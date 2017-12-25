> 概念：实体匹配总的来说是把两个数据项合并为一个，或者把它们一一对应起来。比如把语音识别为文字，就是其中应用之一。

P51

几个概念的理解：

**精度**

精度的计算涉及到召回率与准确度的计算。<br />
书中提到的真阳性、假阳性、真阴性、假阴性。<br />这里的“真”和“假”，是针对猜测结果（或者说是算法计算结果）的正确与否而言的，如果猜对了，就是真，猜错了，就是假。<br />而“阴”和“阳”则是针对猜测结果（或者说是算法计算结果）的正负性质而言的，如果猜测结果是正面，则为阳，猜测结果为负面，则为阴。<br />因此把猜测结果与真实结果做对比，如果**实际为正，猜测为正，则是真阳性**，如果**实际为负，猜测为负，则是真阴性**，如果**实际为正，猜测为负，则是假阴性**，意思是错误地识别为负，如果**实际为负，猜测为正，则是假阳性**，意思是错误地识别为正。

**召回率**的计算公式：

```
召回率 = 真阳性数目 / （真阳性 ＋ 假阴性）
```

实际上就是把正确猜测为正面结果的数量除以所有实际为正面的数量


**准确度**的计算公式：

```
准确度 = 正确猜测数量 / 所有猜测的总数
```

实际上就是把正确地猜测为正面和负面的数量除以所有进行猜测的数目


**特异度**的计算公式：

```
特异度 = 真阴性数目 / 阴性结果数量
```


**精度**的计算公式：

```
精度 = 真阳性数目 / （真阳性数目 + 假阳性数目）
```

实际上就是把正确猜测为正面的数目除以所有猜测为正面的数目，不考虑负面的数目


**F-度量**的计算公式：

```
F1 = 2 * ((精度 x 召回率)) / (精度 + 召回率)
```

**P58页创建数据表的时候要注意！！！**

在Linux下mysql的字段是不区分大小写的，这导致了后面的程序中有插入语句会出现主键重复插入的错误。因为两个地方来的项目名称、URL等，它有可能只是大小写不同，在本项目中，大小写不同，应该是当做两个项目的，但是由于Linux下mysql字段不区分大小写，所以在插入字面相同大小写不同的字段时，会报错。需要在mysql的配置文件中设置大小写敏感。


**P60页**

在这页开始的`for`循环语句，它包含的范围一直到62页的`db.close()`的上一句。而后面的`soundex()`函数应该放在前面


---

### 代理理解


```
# 为了方便起见，每次执行时，我都会先清空结果表，否则重复插入关键值列会报错
cursor.execute("""TRUNCATE TABLE book_entity_matches""")

# 下面这行SQL是把RF和RG中相同URL的项目的名字取出来，放到结果表中
cursor.execute("""INSERT INTO book_entity_matches (
                  rf_project_name, rg_project_name)
                  SELECT rf.project_name, rg.project_name
                  FROM rfrg.book_rf_entities rf
                  INNER JOIN rfrg.book_rg_entities rg
                  ON rf.url = rg.url""")

# 下面这行SQL是把RF和RG中相同名字的项目的名字取出来，放到结果表中
# 同时这些名字应该是不在上一个SQL查询结果中的
cursor.execute("""INSERT INTO book_entity_matches (
                  rf_project_name, rg_project_name)
                  SELECT rf.project_name, rg.project_name
                  FROM rfrg.book_rf_entities rf
                  INNER JOIN book_rg_entities rg
                  ON rf.project_name = rg.project_name
                  WHERE rf.project_name NOT IN (
                      SELECT bem.rf_project_name
                      FROM book_entity_matches bem)""")

# 下面这行SQL把前面两个SQL查询得到的来自两边的项目名称取出
# 同时根据它们的名称在原项目表中取得对应的URL
cursor.execute("""SELECT bem.rf_project_name, bem.rg_project_name, rfe.url, rfe.url
                  FROM rfrg.book_entity_matches bem
                  INNER JOIN rfrg.book_rg_entities rge
                  ON bem.rg_project_name = rge.project_name
                  INNER JOIN rfrg.book_rf_entities rfe
                  ON bem.rf_project_name = rfe.project_name
                  ORDER BY bem.rf_project_name""")
projectPairs = cursor.fetchall()


# 下面对每个名称、URL对进行比较
for (projectPair) in projectPairs:
    RFname = projectPair[0]
    RGname = projectPair[1]
    RFurl = projectPair[2]
    RGurl = projectPair[3]

    # lowercase everything
    RFnameLC = RFname.lower()
    RGnameLC = RGname.lower()
    RFurlLC = RFurl.lower()
    RGurlLC = RGurl.lower()

    # 计算项目名称和URL的编辑距离
    levNames = edit_distance(RFnameLC, RGnameLC)
    levURLs = edit_distance(RFurlLC, RGurlLC)
    soundexRFname = soundex(RFnameLC)
    soundexRGname = soundex(RGnameLC)

    # 如果RF中的项目名字在RG项目中出现了
    # 则把rf_in_rg设置为1，否则为0
    if RFnameLC in RGnameLC:
        rf_in_rg = 1
    else:
        rf_in_rg = 0

    # 如果RF中的URl在RG项目中出现了
    # 则把rf_in_rgurl设置为1，否则为0
    if RFnameLC in RGurl:
        rf_in_rgurl = 1
    else:
        rf_in_rgurl = 0


    # 根据RG项目开发者名称在RF表中提取开发者名称
    cursor.execute("""SELECT rf.dev_username, rf.dev_realname
                      FROM rfrg.book_rf_entity_people rf
                      WHERE rf.project_name = %s
                      AND (rf.dev_username IN (
                          SELECT rg.person_name
                          FROM rfrg.book_rg_entity_people rg
                          WHERE rg.project_name = %s)
                          OR rf.dev_realname IN (
                          SELECT rg.person_name
                          FROM rfrg.book_rg_entity_people rg
                          WHERE rg.project_name = %s))""",
                          (RFname, RGname, RGname))

    result = cursor.fetchone()
    # 如果不为空，说明两者有相同的开发者
    # 则把rfdev_in_rgdev设置为1，否则为0
    if result is not None:
        rfdev_in_rgdev = 1
    else:
        rfdev_in_rgdev = 0


    # 把前面得到的各个标记值更新到结果表中
    # （这样是方便后面的效果检查）
    cursor.execute("UPDATE book_entity_matches \
                      SET rf_name_soundex = %s, \
                          rg_name_soundex = %s, \
                          url_levenshtein = %s, \
                          name_levenshtein = %s, \
                          rf_name_in_rg_name = %s, \
                          rf_name_in_rg_url = %s, \
                          rf_dev_in_rg_dev = %s \
                      WHERE rf_project_name = %s \
                      AND rg_project_name = %s", 
                      (soundexRFname, soundexRGname, levURLs, levNames, rf_in_rg, rf_in_rgurl, rfdev_in_rgdev, RFname, RGname))

```

#### soundex函数解释

这个函数是返回一个单词的声索引。依据是P47中的表。最后把元音和W、Y、H给去掉。<br />
基本原理是设置一个英文字母到数字的映射表。代码中的`digits`列表实现了这个映射

```
def soundex(name, len=4):

    # 设置好字母到数字的映射
    digits = '01230120022455012623010202'
    sndx = ''
    fc = ''

    # 这个for循环把名字中的每个字母变换成对应的声索引的数字
    for c in name.upper():
        if c.isalpha():
            if not fc:
                fc = c      # 把首字母保存下来
            d = digits[ord(c) - ord('A')]   # 根据ASCII码作匹配

            # 如果连续出现两个重复的字母，那么把后一个直接去掉
            # if判断后面的 d != sndx[-1] 实现这个功能
            if not sndx or (d != sndx[-1]):
                sndx += d

    # 把前面保存下来的首字母和后面计算得到的数字连接起来
    sndx = fc + sndx[1:]

    # 把0去掉
    sndx = sndx.replace('0', '')

    # return soundex code padded to len characters
    return (sndx + (len * '0'))[:len]
```

