# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:05:31 2018

@author: Administrator
"""

import gensim.summarization


with open('sampleText.txt') as f:
    text = f.read()

striptext = text.replace('\n\n', ' ')
striptext = striptext.replace('\n', ' ')

summary = gensim.summarization.summarize(striptext, word_count=50)
print(summary)

keywords = gensim.summarization.keywords(striptext)
print(keywords)
