# -*- coding: utf-8 -*-

import gensim.summarization


with open('sampleText.txt') as f:
    text = f.read()

striptext = text.replace('\n\n', ' ')
striptext = striptext.replace('\n', ' ')

summary = gensim.summarization.summarize(striptext, word_count=50)
print(summary)

keywords = gensim.summarization.keywords(striptext)
print(keywords)
