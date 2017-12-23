*这个项目的背景是：有一批开源软件项目，每个项目都带有相应的标签。项目与标签之间是一对多的关系，即一个项目可以有多个标签。这些标签，都是项目里面用到的相关的技术，比如C、C++、JAVA、Python等等。
目的就是通过这一堆项目及其带的标签，找出关联度最高的N个标签组。即哪些标签，是在多数项目中都会出现的。
例如这个项目得到的结果是，Web和Internet这两个标签相互之间的支持度和置信度都非常高，则这个组合就是想要的结果。
而这样子的组合，在本书本项目中，被叫做“项集”
*


**支持度及其计算**

支持度即



P27

> 使用5％的阈值，可以将可能的项集从11006降低为29个。

这里的5％，说的是，出现频率在5％以上的标签，也即书中说到的商品，由后面的`select`语句查询出来的tag\_name，它的出现频率都在5％以上，2335是46510*5%得到的。
说明这46510个篮子中，这此标签的出现频率都在5％以上。

降低到29个。意思是，原来总共有11006个标签，但是出现频率在5％以上的，只有这查询出来的29个。

```
# 设置阈值
MINSUPPORTPCT = 5
allSingletonTags = []
allDoubletonTags = set()
doubletonSet = set()


def findDoubletons():
    print("======")
    print("Frequent doubletons found:")
    print("======")
    # use the list of allSingletonTags to make the doubleton candidates
    doubletonCandidates = list(itertools.combinations(allSingletonTags, 2))
    for (index, candidate) in enumerate(doubletonCandidates):
        # figure out if this doubleton candidate is frequent
        tag1 = candidate[0]
        tag2 = candidate[1]
        cursor.execute("""SELECT count(fpt1.project_id)
                        FROM fc_project_tags fpt1
                        INNER JOIN fc_project_tags fpt2
                        ON fpt1.project_id = fpt2.project_id
                        WHERE fpt1.tag_name = %s
                        AND fpt2.tag_name = %s""", (tag1, tag2))
        count = cursor.fetchone()[0]
        # add frequent doubleton to database
        if count > minsupport:
            print(tag1, tag2, "[", count, "]")
            cursor.execute("""INSERT INTO fc_project_tag_pairs
                            (tag1, tag2, num_projs)
                            VALUES (%s, %s, %s)""", (tag1, tag2, count))

            # save the frequent doubleton to our final list
            doubletonSet.add(candidate)
            # add terms to a set of all doubleton terms (no duplicates)
            allDoubletonTags.add(tag1)
            allDoubletonTags.add(tag2)

def findTripletons():
    print("======")
    print("Frequent tripletons found: ")
    print("======")
    # use the list of all DoubletonTags to make the tripleton candidates
    tripletonCandidates = list(itertools.combinations(allDoubletonTags, 3))

    # sort each candidate tuple and add these to a new sorted candidate list
    tripletonCandidatesSorted = []
    for tc in tripletonCandidates:
        tripletonCandidatesSorted.append(sorted(tc))

    # figure out if this tripleton candidate is frequent
    for (index, candidate) in enumerate(tripletonCandidatesSorted):
        # all doubletons inside this
        # tripleton candidate MUST also be frequent
        doubletonsInsideTripleton = list(itertools.combinations(candidate, 2))
        tripletonCandidateRejected = 0
        for (index, doubleton) in enumerate(doubletonsInsideTripleton):
            if doubleton not in doubletonSet:
                tripletonCandidateRejected = 1
                break
        # add frequent tripleton to database
        if tripletonCandidateRejected == 0:
            cursor.execute("""SELECT count(fpt1.project_id)
                            FROM fc_project_tags fpt1
                            INNER JOIN fc_project_tags fpt2
                            ON fpt1.project_id = fpt2.project_id
                            INNER JOIN fc_project_tags fpt3
                            ON fpt2.project_id = fpt3.project_id
                            WHERE (fpt1.tag_name = %s
                            AND fpt2.tag_name = %s
                            AND fpt3.tag_name = %s)""", (candidate[0], candidate[1], candidate[2]))
            count = cursor.fetchone()[0]
            if count > minsupport:
                print(candidate[0], ",",
                        candidate[1], ",",
                        candidate[2],
                        "[", count, "]")
                cursor.execute("""INSERT INTO fc_project_tag_triples
                                (tag1, tag2, tag3, num_projs)
                                VALUES (%s, %s, %s, %s)""",
                                (candidate[0],
                                 candidate[1],
                                 candidate[2],
                                 count))


def generateRules():
    print("======")
    print("Association Rules:")
    print("======")

    # pull final list of tripletons to make the rules
    cursor.execute("SELECT tag1, tag2, tag3, num_projs FROM fc_project_tag_triples")
    triples = cursor.fetchall()
    for (triple) in triples:
        tag1 = triple[0]
        tag2 = triple[1]
        tag3 = triple[2]
        ruleSupport = triple[3]

        calcSCAV(tag1, tag2, tag3, ruleSupport)
        calcSCAV(tag1, tag3, tag2, ruleSupport)
        calcSCAV(tag2, tag3, tag1, ruleSupport)
        print("*")

def calcSCAV(tagA, tagB, tagC, ruleSupport):
    # Support
    ruleSupportPct = round((ruleSupport/baskets), 2)

    # Confidence
    query1 = "SELECT num_projs FROM fc_project_tag_pairs WHERE (tag1 = %s AND tag2 = %s) or (tag2 = %s AND tag1 = %s)"
    cursor.execute(query1, (tagA, tagB, tagB, tagA))
    pairSupport = cursor.fetchone()[0]
    confidence = round((ruleSupport / pairSupport), 2)

    # Added Value
    query2 = "SELECT count(*) FROM fc_project_tags WHERE tag_name = %s"
    cursor.execute(query2, tagC)
    supportTagC = cursor.fetchone()[0]
    supportTagCPct = supportTagC/baskets
    addedValue = round((confidence - supportTagCPct), 2)

    # Result
    print(tagA, ",", tagB, "->", tagC,
          "[S=", ruleSupportPct,
          ", C=", confidence,
          ", AV=", addedValue,
          "]")

# 程序从这里开始运行
# 下面这个查询是得到项目的总数
queryBaskets = "SELECT count(DISTINCT project_id) FROM fc_project_tags;"
cursor.execute(queryBaskets)
baskets = cursor.fetchone()[0]

minsupport = baskets * (MINSUPPORTPCT / 100)
print("Mininum support count:", minsupport, "(", MINSUPPORTPCT, "%of", baskets, ")")

cursor.execute("SELECT DISTINCT tag_name FROM fc_project_tags GROUP BY 1 HAVING COUNT(project_id) >= %s ORDER BY tag_name", (minsupport))
singletons = cursor.fetchall()

for (singleton) in singletons:
    allSingletonTags.append(singleton[0])

findDoubletons()
findTripletons()
generateRules()
db.close()
```

