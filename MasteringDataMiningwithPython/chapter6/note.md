#命名实体识别

命名实体识别（Named Entity Reconize, NER）指的是在文本中识别出表示特定目标对象的词语。如专有名词。类似的可以想象百科词条。在百度百科词条中，人们可以为特定的词去添加上对应的百科超链接，这些词通常就是专有名词，这也属于命名实体识别的一种。


## 英文中命名实体识别存在的问题

* 专有名词和名称未必都大写
* 大写的词未必都是专有名词
* 命名实体会有歧义，它包含有固定指示词和非固定指示词，如：周三、美国总统。它们都是专有名词，但具体所指未必都是相同的
* 非固定指示词也有可能大写


## 常见命名实体类型

* 个人(PERSON)
* 组织(ORGANZATION)
* GPE (地理学或者地点实体)


## NER系统的构建步骤

1) 将文档分割为句子
2) 将句子分割为单词
3) 标记每个单词的词性
4) 从标记单词集中识别命名实体
5) 识别每个命名裕的分类


## NER系统的评估

**严格评分**

将部分匹配同时当成假阳性和假阴性来评分

**宽松评分**

将部分匹配当成真阳性，对假阴性或者假阳性不做任何重罚。

**部分评分**

提出规则，为部分正确的匹配给出某种分数。如边界正确给1分，分类正确给1分

*所谓**边界**，即给专有名词划分的边界。如微软的操作系统名为Microsoft Windows，如果完整地识别出这两个单词为一个实体，那边界是对的，如果只识别出Microsoft，那么边界是不对的。所谓**分类**，即把这个识别出来的名词归类（个人、组织或者地理学地点等）*


**指标及计算方式**

CORRECT：边界和分类的正确猜测次数之和
GUESSED：边界和分类的实际回答次数之和
POSSIBLE：边界和分类的可能回答次数之和


> 精度

```
Precision = CORRECT / GUESSED
```

> 召回率

```
Recall = CORRECT / POSSIBLE
```

> F1

```
F1 = 2 * ((Precision * Recall) / (Precision + Recall))
```


# 代码理解

```
# 设置测试文件名
filename = 'apacheMeetingMinutes.txt'
#filename = 'djangoIRCchat.txt'
#f1ilename = 'gnueIRCsummary.txt'
#filename = 'lkmlEmails.txt'
#filename = 'lkmlEmailsReduced.txt'

# 打开测试文件，读入里面的内容
with open(filename, 'r', encoding='utf8') as sampleFile:
    text = sampleFile.read()

# en是个字典，用来保存结果
en = {}
try:
    # 这里的english.pickle模块是一个英文句子边界检测器，已经由NLTK训练好了的
    # 没有针对中文的模块
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    # 把文件内的内容识别为一条条句子
    sentences = sent_detector.tokenize(text.strip())
    
    for sentence in sentences:
        # 把每条句子分割为单词
        tokenized = nltk.word_tokenize(sentence)
        # 进行词性标注
        tagged = nltk.pos_tag(tokenized)
        # 进行命名实体识别
        chunked = nltk.ne_chunk(tagged)
        for tree in chunked:
            # 如果节点有label这个属性，说明它被识别为实体了
            if hasattr(tree, 'label'):
                # 保存单词本身
                ne = ' '.join(c[0] for c in tree.leaves())
                # 保存单词对应的属性标签
                en[ne] = [tree.label(), ' '.join(c[1] for c in tree.leaves())]
except Exception as e:
    print(str(e))

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(en)
```
