**情感分析的难题之一**

计算机难以处理含蓄的话语，如：

```
如果你在周六晚上没事可干，那么应该去看看《小美人鱼》，但是洗洗头发或者整理一下装袜子的抽屉可能更好。
```

这句话其实意思是《小美人鱼》这部电影不值一看，是贬义的。但是句子里面并没有出现明显贬义的词。

**情感分析的难题之二**

并不是每个领域都以相同的方式对待同一个词，一个领域中表示贬义的词在另一个领域却并不一定是贬义。

**情感分析的难题之三**

词语在文本中的位置的不同，可能会产生相反的含义。但整体而言，组成句子的词语是并没有改变的，只是顺序变了

**情感分析的难题之四**

与三类似，否定词的出现也是如此。


**朴素贝叶斯分类器**

训练数据非常重要，会直接影响整个方案的效果。并且如果训练数据过于一般化或者训练过于紧密，则容易造成欠拟合和过拟合。


**Vader情感分析工具中的复合得分计算公式**

复合得分是加入标点强调得分、得分相应增大之后正面和负面得分的规格化总和。这里的alpha值为15

```
compound = score / math.sqrt((score * score) + alpha)
```

**P128**

页面中的SQL语句使用到的表名错误，应该是作者给出的SQL脚本中所创建的`lkml_ch5`表



## 代码理解


> scoreSenntences.py

```
with open('data/ubuntu2016-04-04/ubuntu.txt', encoding='utf-8') as ubuntu:
    ubuntuLines = [line.strip() for line in ubuntu.readlines()]
ubuntu.close()

sid = SentimentIntensityAnalyzer()
finalScore = 0

for line in ubuntuLines[0:20]:
    print(line)
    
    # 这里的polarity_scores方法会返回一个字典型对象。
    # 在这时，这个返回值包含了复合得分、正面得分、中性得分、负面得分
    ss = sid.polarity_scores(line)
    # 这里的for循环把返回的内容都打印出来
    for k in sorted(ss):
        print(' {0}: {1}\n'.format(k, ss[k]), end='')
    print()
```


> sumCompounds.py

```
# 这里的ubuntuLines, ubuntuDevelLines都是列表对象
# 下面这行代码是把这两个列表放一起了
listOfChannels = [ubuntuLines, ubuntuDevelLines]

sid = SentimentIntensityAnalyzer()

# 循环历遍这两个不同类别的聊天内容
for channel in listOfChannels:

    # 这个finalScore用来记录每个类别的总得分
    finalScore = 0

    # 循环历遍每个类别中的每一行聊天内容
    for line in channel:
        # 取得所有得分项
        ss = sid.polarity_scores(line)
        # 取得复合得分
        score = ss['compound']
        # 复合得分累加
        finalScore = finalScore + score
    # 用最后得到的复合得分项除以类别中所有句子总和（类别列表长度）
    # 书中下面一行使用了缩进，属于for循环内部。但其实没什么必要
    roundedFinalScore = round(finalScore / len(channel), 4)
    print("Score", roundedFinalScore)
```

> scoreLinusEmail.py

```
# 这里获取了两个游标对象，分别用于执行查询和更新语句
selectCursor = db.cursor()
updateCursor = db.cursor()

# 把查询语句写好
selectEmailQuery = "SELECT url, body FROM lkml_ch5"
# 这里的更新语句只是个模板
updateScoreQuery = "UPDATE lkml_ch5 \
                    SET sentiment_score = %s, \
                    max_pos_score = %s, \
                    max_neg_score = %s, \
                    WHERE url = %s"

# 执行查询
selectCursor.execute(selectEmailQuery)
# 取得查询返回的所有结果
emails = selectCursor.fetchall()


# 循环历遍每封邮件
for email in emails:
    
    # 取出邮件URL地址和邮件内容
    url = email[0]
    body = email[1]

    # 这两个变量用来保存最终结果以及四舍五入后的结果
    finalScore = 0
    roundedFinalScore = 0

    # 这两个变量用于保存每封邮件中，正面得分最大的值以及负面得分最大的值
    maxPosScore = 0
    maxNegScore = 0

    sid = SentimentIntensityAnalyzer()
    
    # tokenize.sent_tokenize的作用是把一段文本切割成句子，返回句子列表
    # 类似的还有word_tokenize
    emailLines = tokenize.sent_tokenize(body)
    # 循环历遍每个句子
    for line in emailLines:
        ss = sid.polarity_scores(line)
        # 把句子中的换行符替换
        line = line.replace('\n', ' ').replace('\r', '')
        print(line)
        for k in sorted(ss):
            print(' {0}: {1}\n'.format(k, ss[k]), end='')
        # 取得句子的复合得分
        lineCompoundScore = ss['compound']
        # 复合得分累加
        finalScore += lineCompoundScore

        # 判断句子的正面／负面得分是否比过去的更大
        # 如果是的话，就把更大的值保存
        if ss['pos'] > maxPosScore:
            maxPosScore = ss['pos']
        elif ss['neg'] > maxNegScore:
            maxNegScore = ss['neg']
        
    # 计算最终的复合得分
    roundedFinalScore = round(finalScore / len(emailLines), 4)

    # 把结果保存到数据库中
    try:
        updateCursor.execute(updateScoreQuery, (roundedFinalScore, maxPosScore, maxNegScore, url))
        db.commit()
    except:
        db.rollback()
```
