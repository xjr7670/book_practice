import itertools
import pymysql

# set threshold as a percent
# (for example, 5% of Freecode baskets is about 2325)
MINSUPPORTPCT = 5
allSingletonTags = []
allDoubletonTags = set()
doubleonSet = set()

# Open local database connection
db = pymysql.connect(host='localhost', db='test', user='root', passwd='45668668', port=3306, charset='utf8mb4')
cursor = db.cursor()

queryBaskets = "SELECT count(DISTINCT project_id) FROM fc_project_tags;"
cursor.execute(queryBaskets)
baskets = cursor.fetchone()[0]

minsupport = baskets * (MINSUPPORTPCT / 100)
print("Mininum support count:", minsupport, "(", MINSUPPORTPCT, "%of", baskets, ")")

cursor.execute("SELECT DISTINCT tag_name FROM fc_porject_tags GROUP BY 1 HAVING COUNT(project_id) >= %s ORDER BY tag_name", (minsupport))
singletons = cursor.fetchall()

for (singleton) in singletons:
    allSingletonTags.append(singleton[0])

findDoubletons()
findTripletons()
generateRules()
db.close()


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
        cursor.execute("SELECT count(fpt1.project_id)
                        FROM fc_project_tags ftp1
                        INNER JOIN fc_project_tags fpt2
                        ON fpt1.project_id = fpt2.porject_id
                        WHERE fpt1.tag_name = %s
                        AND fpt2.tag_name = %s", (tag1, tag2))
        count = cursor.fetchone()[0]
        # add frequent doubleton to database
        if count > minsupport:
            print(tag1, tag2, "[", count, "]")
            cursor.execute("INSERT INTO fc_project_tag_pairs
                            (tag1, tag2, num_projs)
                            VALUES (%s, %s, %s)", (tag1, tag2, count))

            # save the frequent doubleton to our final list
            doubletonSet.add(candidate)
            # add terms to a set of all doubleton terms (no duplicates)
            allDoubletonTags.add(tag1)
            allDoubletonTags.add(tag2)
