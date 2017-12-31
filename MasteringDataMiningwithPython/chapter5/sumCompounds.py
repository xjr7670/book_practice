#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 21:49:32 2017

@author: cavin
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer

ubuntu_data_loc = "./data/ubuntu2016-04-04/"

with open(ubuntu_data_loc + 'ubuntu.txt', encoding='utf-8') as ubuntu:
    ubuntuLines = [line.strip() for line in ubuntu.readlines()]
ubuntu.close()


with open(ubuntu_data_loc + 'ubuntu-devel.txt', encoding='utf-8') as ubuntuDevel:
    ubuntuDevelLines = [line.strip() for line in ubuntuDevel.readlines()]
ubuntuDevel.close()


listOfChannels = [ubuntuLines, ubuntuDevelLines]
sid = SentimentIntensityAnalyzer()

for channel in listOfChannels:
    finalScore = 0
    for line in channel:
        ss = sid.polarity_scores(line)
        score = ss['compound']
        finalScore = finalScore + score
    roundedFinalScore = round(finalScore/len(channel), 4)
    print("Score", roundedFinalScore)
