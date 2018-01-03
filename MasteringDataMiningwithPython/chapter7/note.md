# 第7章 自动化文本摘要


## 使用NLTK的简单文本摘要

```
# 读入样本文本
with open('sampleText.txt', encoding='utf-8') as f:
    text = f.read()

summary_sentences = []
candidate_sentences = {}
candidate_sentence_counts = {}

# 把样本文本进行分词
words = word_tokenize(striptext)
# 过滤停用词与非字母词，并全部变成小写形式
lowercase_words = [word.lower() for word in words 
        if word not in stopwords.words() and word.isalpha()]

word_frequencies = FreqDist(lowercase_words)
# FreqDist函数返回单词的频率分布。返回值为二元元组：词和出现次数
most_frequent_words = FreqDist(lowercase_words).most_common(20)

# 把删除回车符后的文本分割为句子，返回列表
sentences = sent_tokenize(striptext)
for sentence in sentences:
    # 以句子本身为键，它的全小写形式为值保存
    candidate_sentences[sentence] = sentence.lower()

for long, short in candidate_sentences.items():
    count = 0

    # 历遍所有高频词
    for freq_word, frequency_score in most_frequent_words:
        # 如果高频词出现在句子中
        if freq_word in short:
            # 则句子的得分增加
            count += frequency_score
            candidate_sentence_counts[long] = count

# 排序。得到降序排列后的字典对象
sorted_sentences = OrderedDict(sorted(
                                candidate_sentence_counts.items(),
                                key = lambda x: x[1],
                                reverse = True)[:4])
```


## 使用Gensim的文本摘要

Gensim的文本摘要方法使用的是TextRank。它提取的是相似性得分高的句子，相似性由两个句子共享的常见词法标记数量计算。

**代码理解**

```

# 读入样本文本
with open('sampleText.txt') as f:
    text = f.read()

# 获得摘要文本
summary = gensim.summarization.summarize(striptext, word_count=50)

# 获得重点关键词
keywords = gensim.summarization.keywords(striptext)

*具体理论方法尚未完全弄明白，惭愧*

```


##使用sumy的文本摘要


```
# 设置分词、分句语言和最终摘要句子的数量
LANGUAGE = 'english'
SENTENCES_COUNT = 4

# 获得样本文件对象，分句
parser = PlaintextParser.from_file("sampleText.txt", Tokenizer(LANGUAGE))
# 利用sumy中的Stemmer方法进行词干分析
# 所谓词干分析，是把词的变形给统一化。如：fishing -> fish
stemmer = Stemmer(LANGUAGE)


## 使用Luhn方法
print("\n===== Luhn =====")
summarizerLuhn = LuhnSummarizer(stemmer)
summarizerLuhn.stop_words = get_stop_words(LANGUAGE)
for sentenceLuhn in summarizerLuhn(parser.document, SENTENCES_COUNT):
    print(sentenceLuhn, "\n")


## 使用TextRank算法
print("\n===== TextRank =====")
summarizerTR = TextRankSummarizer(stemmer)
summarizerTR.stop_words = get_stop_words(LANGUAGE)
for sentenceTR in summarizerTR(parser.document, SENTENCES_COUNT):
    print(sentenceTR, "\n")


## 使用LSA算法
# 它使用了潜在语义分析。基本思路是：
#   用LSA建立一个矩阵，行代表词，列代表句子。
#   行和列的交叉点是每个词在每个句子中出现的次数。
#       相似度计算方法：从数学上简化矩阵，然后比较简化矩阵中向量角的余弦，找出相似的行
print("\n===== LSA =====")
summarizerLSA = LsaSummarizer(stemmer)
summarizerLSA.stop_words = get_stop_words(LANGUAGE)
for sentenceLSA in summarizerLSA(parser.document, SENTENCES_COUNT):
    print(sentenceLSA, "\n")


## 使用Edmundson算法
# 它可以注入某些词语，作为与兔子重要性高度相关的标语
# 所以要先设置褒义词、贬义词和无效词列表
print("\n===== Edmonson =====")
summarizerEd = EdmundsonSummarizer(stemmer)
summarizerEd.bonus_words = ('focus', 'proposed', 'method', 'describes')
summarizerEd.stigma_words = ('example')
summarizerEd.null_words = ('literature', 'however')
for sentenceEd in summarizerEd(parser.document, SENTENCES_COUNT):
    print(sentenceEd, "\n")
```
