#!/usr/bin/env python
#-*- coding:utf-8 -*-


from gensim import corpora
from gensim.models.ldamodel import LdaModel
from gensim.parsing.preprocessing import STOPWORDS
import pprint


num_topics = 4
num_words = 5
passes = 100


#filename = 'data/introSectionsToChapters.txt'
#filename = 'data/sampleTextFromCh7.txt'
#filename = 'data/gnueIRCsummary.txt'
#filename = 'data/apacheMeetingMinutes.txt'
#filename = 'data/lkmlLinusJan2016.txt'
filename = 'data/lkmlLinusJan2006.txt'
#filename = 'data/lkmlLinusAll.txt'


with open(filename, encoding='utf-8') as f:
    documents = f.readlines()

texts = [[word for word in document.lower().split()
        if word not in STOPWORDS and word.isalnum()]
        for document in documents]

dictionary = corpora.Dictionary(texts)
dictionary.save('lkml.dict')
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('lkml.mm', corpus)

lda = LdaModel(corpus, id2word=dictionary, num_topics=num_topics, passes=passes)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(lda.print_topics(num_words=num_words))
lda.save('lkml.gensim')
#newlda = LdaModel.load('lkml.gensim', mmap='r')
#pp.pprint(lda.print_topics(num_words=num_words))


unseenText = 'data/lkmlSingleNewEmail.txt'
with open(unseenText, encoding='utf-8') as fnew:
    newdoc = fnew.read()

newcorpus = dictionary.doc2bow(newword for newword in newdoc.lower().split()
                                if newword not in STOPWORDS and newword.isalnum())
pp.pprint(lda[newcorpus])
