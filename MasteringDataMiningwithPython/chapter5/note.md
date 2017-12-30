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

# just print the first 20 lines of the chat log & score
for line in ubuntuLines[0:20]:
    print(line)
    
    # 这里的polarity_scores方法会返回两个值，一个是正面得分，另一个是负面得分
    ss = sid.polarity_scores(line)
    for k in sorted(ss):
        print(' {0}: {1}\n'.format(k, ss[k]), end='')
    print()
```
