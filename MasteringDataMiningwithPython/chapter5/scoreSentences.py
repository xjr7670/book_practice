#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 21:27:21 2017

@author: cavin
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer


with open('data/ubuntu2016-04-04/ubuntu.txt', encoding='utf-8') as ubuntu:
    ubuntuLines = [line.strip() for line in ubuntu.readlines()]
ubuntu.close()

sid = SentimentIntensityAnalyzer()
finalScore = 0

# just print the first 20 lines of the chat log & score
for line in ubuntuLines[0:20]:
    print(line)
    ss = sid.polarity_scores(line)
    for k in sorted(ss):
        print(' {0}: {1}\n'.format(k, ss[k]), end='')
    print()