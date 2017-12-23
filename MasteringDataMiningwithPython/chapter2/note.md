*这个项目的背景是：有一批开源软件项目，每个项目都带有相应的标签。项目与标签之间是一对多的关系，即一个项目可以有多个标签。这些标签，都是项目里面用到的相关的技术，比如C、C++、JAVA、Python等等。<br />目的就是通过这一堆项目及其带的标签，找出关联度最高的N个标签组。即哪些标签，是在多数项目中都会出现的。<br />例如这个项目得到的结果是，Web和Internet这两个标签相互之间的支持度和置信度都非常高，则这个组合就是想要的结果。<br />而这样子的组合，在本书本项目中，被叫做“项集”*


**支持度及其计算**

支持度即某个项集出现在所有篮子中的频率。如(C, C++)这个项集的支持度是所有同时带有这两个标签的项目个数除以项目总数量。<br />
记为：

```
support(X->Y) = P(XuY)
```

支持度越高，说明这个组合的出现频率越高<br />
后面的设置阈值，就是要把一些频率过低的组合给过滤掉，不考虑它们。

**置信度及其计算**

所有项目中，使用C同时使用Python的可能会很多，但是使用Python但同时也使用C的可能就很少了。<br />
这就需要引入置信度的计算。<br />
置信度的记法：

```
confidence(X->Y) = P(Y|X) = support(XuY) / support(X)
```

解释为：同时包含X标签和Y标签的项目的百分比除以只包含标签X的百分比


**关联规则**

由支持度与置信度联合，可得关联规则：

```
C -> C++, Python
[支持度=1%, 置信度=40%]
```

解释为：在所有项目中，有1％同时使用了C、C++、Python；在使用C的所有项目中，有40％同时使用了C++和Python


**附加值**

在书中的商品的例子中，单独买香蕉的人比同时购买香蕉和香草威化的人多得多（支持度更高）。<br />
这说明有些商品自身的表现好于作为关联规则后继时的表现。因此要增加一个附加值<br />
计算公式

```
X->Y 的附加值 = 规则置信度 - Y的支持度
```

附加值为大的正数，说明规则是好的，有用的。如果接近于0，说明它是正确的，但没什么帮助。如果是大的负数，说明商品是负相关的，单独使用会更好。

这个也叫“兴趣度”




P27

> 使用5％的阈值，可以将可能的项集从11006降低为29个。

这里的5％，说的是，出现频率在5％以上的标签，也即书中说到的商品，由后面的`select`语句查询出来的tag\_name，它的出现频率都在5％以上，2335是46510*5%得到的。
说明这46510个篮子中，这此标签的出现频率都在5％以上。

降低到29个。意思是，原来总共有11006个标签，但是出现频率在5％以上的，只有这查询出来的29个。


### 代码理解

*下面的代码中已经略去了一部分*

```
MINSUPPORTPCT = 5           # 设置阈值
allSingletonTags = []       # 把所有标签都取出来，放在列表中
allDoubletonTags = set()    # 所有的二元组，集合类型
doubletonSet = set()        # 大于阈值的二元组，集合类型


def findDoubletons():
    
    # itertools.combinations这个函数可以生成组合
    # 它接收两个参数，第1个参数是一个可迭代对象，由它来构成组合的元素
    # 第2个参数是一个数字，用于指明生成的元素中包含多少个子元素
    # 所以下面一行生成一个由二元元组组成的列表
    # 这个列表中的每个元素都是由满足最小阈值要求的标签组成的
    doubletonCandidates = list(itertools.combinations(allSingletonTags, 2))


    # 循环历遍每一个标签组进行计算比较
    for (index, candidate) in enumerate(doubletonCandidates):
        # figure out if this doubleton candidate is frequent
        tag1 = candidate[0]
        tag2 = candidate[1]
       
        # 下面这个SQL查询语句，是用于查询所有项目中
        # 同时包含tag1和tag2这两个标签的项目个数有多少
        cursor.execute("""SELECT count(fpt1.project_id)
                        FROM fc_project_tags fpt1
                        INNER JOIN fc_project_tags fpt2
                        ON fpt1.project_id = fpt2.project_id
                        WHERE fpt1.tag_name = %s
                        AND fpt2.tag_name = %s""", (tag1, tag2))
        count = cursor.fetchone()[0]



        # 如果同时包含这两个标签的项目数量大于最小支持阈值的话
        # 就把这两个标签组和它们的出现次数插入到表fc_project_tag_pairs中
        if count > minsupport:
            print(tag1, tag2, "[", count, "]")
            cursor.execute("""INSERT INTO fc_project_tag_pairs
                            (tag1, tag2, num_projs)
                            VALUES (%s, %s, %s)""", (tag1, tag2, count))

            # 把这个满足条件要求的二元元组加到二元组的结果集合中
            # 这个结果后面直接用于输出了
            doubletonSet.add(candidate)

            # 同时把满足条件要求的这两个标签加入到包含所有满足条件的二元组标签的集合中
            # 这个集合是为了方便后面提取三元元组
            allDoubletonTags.add(tag1)
            allDoubletonTags.add(tag2)

def findTripletons():
"""
查找三元元组的函数与查找二元元组的函数类似
不过它多了一个判断功能，就是它得到的三元元组集合中，每个三元元组中的元素的两两组合，都应该是出现于二元元组结果集合中的
因此又可以再过滤掉一部分标签，使提取精度得到提高
"""

    # 下面一行生成一个由三元元组组成的列表
    # 这个列表中的每个元素都是由满足最小阈值要求的标签组成的，而这些标签，都是由前面的查找二元元组的函数生成的
    tripletonCandidates = list(itertools.combinations(allDoubletonTags, 3))


    # 下面这三行代码把上一行中得到的候选三元元组列表进行了排序
    # 得到一个排序后的三元元组列表
    tripletonCandidatesSorted = []
    for tc in tripletonCandidates:
        tripletonCandidatesSorted.append(sorted(tc))


    # 循环历遍每个三元元组列表中的元素（是一个三元元组对象）
    for (index, candidate) in enumerate(tripletonCandidatesSorted):

        doubletonsInsideTripleton = list(itertools.combinations(candidate, 2))  # 得到由三元元组组成的二元元组列表
        tripletonCandidateRejected = 0                                          # 设置一个标记，如果不存在于频繁二元元组（即结果集）中，则为1
        for (index, doubleton) in enumerate(doubletonsInsideTripleton):         # 判断这个三元元组中的元素的两两组合，是否都属于频繁二元元组
            if doubleton not in doubletonSet:
                tripletonCandidateRejected = 1
                break                                                           # 只要其中某一个组合不属于频繁二元元组，则跳过



        # 如果都是频繁二元组，则查询同时包含这三个标签的项目数量
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

            # 如果这个数量大于最小支持阈值
            # 则把这三个标签和它们的出现次数插入到表fc_project_tag_triples中
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
"""
计算并打印三元元组的关联规则
"""

    # 从三元组表中查询出所有的结果集
    cursor.execute("SELECT tag1, tag2, tag3, num_projs FROM fc_project_tag_triples")
    triples = cursor.fetchall()

    # 历遍它
    for (triple) in triples:
        tag1 = triple[0]
        tag2 = triple[1]
        tag3 = triple[2]
        ruleSupport = triple[3]

        # 计算两两之间的关联规则数据
        calcSCAV(tag1, tag2, tag3, ruleSupport)
        calcSCAV(tag1, tag3, tag2, ruleSupport)
        calcSCAV(tag2, tag3, tag1, ruleSupport)
        print("*")

def calcSCAV(tagA, tagB, tagC, ruleSupport):

    # 计算支持度
    # 等于满足条件要求的项目数量除以总的项目数量
    ruleSupportPct = round((ruleSupport/baskets), 2)

    
    # 计算置信度

    # 下面的语句在包在频繁二元元组数据的表中查询同时出现标签1和标签2的项目个数
    query1 = "SELECT num_projs FROM fc_project_tag_pairs WHERE (tag1 = %s AND tag2 = %s) or (tag2 = %s AND tag1 = %s)"
    cursor.execute(query1, (tagA, tagB, tagB, tagA))
    pairSupport = cursor.fetchone()[0]
    # 置信度的计算
    # ruleSupport是同时包含三个标签的项目数量
    # 这个计算是符合前面的置信度计算公式的
    confidence = round((ruleSupport / pairSupport), 2)


    # 计算附加值

    # 下面的语句在包含所有项目数据的表中查询包含标签3的项目的个数
    query2 = "SELECT count(*) FROM fc_project_tags WHERE tag_name = %s"
    cursor.execute(query2, tagC)
    supportTagC = cursor.fetchone()[0]
    # 计算标签3的支持度
    # 等于出现标签3的项目个数除以所有项目个数
    supportTagCPct = supportTagC/baskets
    # 置信度减去标签3的支持度，即可得到附加值
    addedValue = round((confidence - supportTagCPct), 2)


    # 打印结果
    print(tagA, ",", tagB, "->", tagC,
          "[S=", ruleSupportPct,
          ", C=", confidence,
          ", AV=", addedValue,
          "]")

# 程序从这里开始运行
# 下面这个查询是得到项目的总数，得到一个数字，方便后面的计算
queryBaskets = "SELECT count(DISTINCT project_id) FROM fc_project_tags;"
cursor.execute(queryBaskets)
baskets = cursor.fetchone()[0]


# 得到阈值支持数量。即这个标签至少在所有项目中出现多少次以上，才把它用于计算
minsupport = baskets * (MINSUPPORTPCT / 100)
print("Mininum support count:", minsupport, "(", MINSUPPORTPCT, "%of", baskets, ")")


# 把出现次数大于最小数量的标签取出来
cursor.execute("SELECT DISTINCT tag_name FROM fc_project_tags GROUP BY 1 HAVING COUNT(project_id) >= %s ORDER BY tag_name", (minsupport))
singletons = cursor.fetchall()

# 把满足最小阈值数量要求的标签取出来，放到allSingletonTags列表中
for (singleton) in singletons:
    allSingletonTags.append(singleton[0])

findDoubletons()    # 查找符合条件的二元组
findTripletons()    # 查找符合条件的三元组
generateRules()     # 产生规则。打印出来
db.close()
```

得到结果之后，检查所有结果的支持度、置信度、附加值。<br />
这三个指标都为正且值越大，说明结果越有价值



















------------------------------------------------

本书中，最终发现关联度最为密切的是`Web`和`Internet`这两个标签。于是进一步深入挖掘它们之间的联系


```
X = 'Internet'
Y = 'Web'


# 查询出所有项目数量
numBasketsQuery = "SELECT count(DISTINCT project_id) FROM fc_project_tags"
cursor.execute(numBasketsQuery)
numBaskets = cursor.fetchone()[0]


# 查询包含X即Internet标签的项目数量
supportForXQuery = "SELECT count(*) FROM fc_project_tags WHERE tag_name=%s"
cursor.execute(supportForXQuery, (X))
supportForX = cursor.fetchone()[0]


# 查询包含Y即Web标签的项目数量
supportForYQuery = "SELECT count(*) FROM fc_project_tags WHERE tag_name=%s"
cursor.execute(supportForYQuery, (Y))
supportForY = cursor.fetchone()[0]


# 查询同时包含X和Y标签的项目数量
pairSupportQuery = "SELECT num_projs FROM fc_project_tag_pairs WHERE tag1=%s AND tag2=%s"
cursor.execute(pairSupportQuery, (X, Y))
pairSupport = cursor.fetchone()[0]



# 计算支持度
# 即同时包含两个标签的项目数量除以所有项目数量
pairSupportAsPct = pairSupport / numBaskets

# 计算X到Y的置信度
# 即同时包含两个标签的项目数量比例除以X标签的支持度
supportForXAsPct = supportForX / numBaskets
confidenceXY = pairSupportAsPct / supportForXAsPct

# 计算Y到X的置信度
# 即同时包含两个标签的项目数量比例除以所有包含Y标签的项目数量
supportForYAsPct = supportForY / numBaskets
confidenceYX = pairSupportAsPct / supportForYAsPct

# 计算X到Y的附加值
# 即X到Y的置信度减去Y的支持度
AVXY = confidenceXY - supportForYAsPct

# 计算Y到X的附加值
# 即Y到X的置信度减去X的支持度
AVYX = confidenceYX - supportForXAsPct

print("Support for ", X, "U", Y, ":", round(pairSupportAsPct, 2))
print("Conf.", X, "->", Y, ":", round(confidenceXY, 2))
print("Conf.", Y, "->", X, ":", round(confidenceYX, 2))
print("AV", X, "->", Y, ":", round(AVXY, 2))
print("AV", Y, "->", X, ":", round(AVYX, 2))
```
