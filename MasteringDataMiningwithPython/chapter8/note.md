# 第8章 文本中的主题建模

所谓主题建模，就是从一堆文本中找出它们都在讲些什么，即主题是什么。


## 潜在狄利克雷分配（LDA）

这是文本主题建模中最常用的技术。它主要是根据单词在文本中出现的概率做判断的。

**代码理解**

```

# 设置最终要获取的主题个数
num_topics = 4
# 每个主题包含的关键词数量
num_words = 5
# 迭代计算次数
passes = 100


# 设置不同的文件以观察不同类型文本的结果
#filename = 'data/introSectionsToChapters.txt'
#filename = 'data/sampleTextFromCh7.txt'
#filename = 'data/gnueIRCsummary.txt'
#filename = 'data/apacheMeetingMinutes.txt'
#filename = 'data/lkmlLinusJan2016.txt'
filename = 'data/lkmlLinusJan2006.txt'
#filename = 'data/lkmlLinusAll.txt'


with open(filename, encoding='utf-8') as f:
    documents = f.readlines()

# 取出文本中的所有单词，并变为小写，同时去除停用词和符号
texts = [[word for word in document.lower().split()
        if word not in STOPWORDS and word.isalnum()]
        for document in documents]

# 用单词来创建字典。键为单词
dictionary = corpora.Dictionary(texts)
# 保存字典对象为文件，
dictionary.save('lkml.dict')
# doc2bow函数把每个词都放到词袋中计数和保存。返回二元元组（单词，个数）
corpus = [dictionary.doc2bow(text) for text in texts]
# 保存语料库
corpora.MmCorpus.serialize('lkml.mm', corpus)

# 建立LDA模型
lda = LdaModel(corpus, id2word=dictionary, num_topics=num_topics, passes=passes)

pp = pprint.PrettyPrinter(indent=4)

# 打印LDA主题
pp.pprint(lda.print_topics(num_words=num_words))

# 保存LDA主题模型
lda.save('lkml.gensim')
#newlda = LdaModel.load('lkml.gensim', mmap='r')
#pp.pprint(lda.print_topics(num_words=num_words))

# 利用前面训练好的模型来给新文本进行主题分类
unseenText = 'data/lkmlSingleNewEmail.txt'
with open(unseenText, encoding='utf-8') as fnew:
    newdoc = fnew.read()

newcorpus = dictionary.doc2bow(newword for newword in newdoc.lower().split()
                                if newword not in STOPWORDS and newword.isalnum())

# 打印出来的是新文本对就模型中的各个主题的匹配率。值越大表示越相近
pp.pprint(lda[newcorpus])
```

LDA模型出来的结果里，每个主题里面的单词前面的数字表示这个单词的贡献率。

使用不同的单词数和主题数，会得到不同的结果，而且迭代的次数不同得到的结果也不同


