#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:08:18 2017

@author: cavin
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import pymysql
import sys


db = pymysql.connect(host='localhost',
        db='test',
        user='root',
        passwd='45668668',
        port=3306,
        charset='utf8mb4')
selectCursor = db.cursor()
updateCursor = db.cursor()

selectEmailQuery = "SELECT url, body FROM lkml_ch5"
updateScoreQuery = "UPDATE lkml_ch5 \
                    SET sentiment_score = %s, \
                    max_pos_score = %s, \
                    max_neg_score = %s, \
                    WHERE url = %s"
selectCursor.execute(selectEmailQuery)
emails = selectCursor.fetchall()


for email in emails:
    url = email[0]
    body = email[1]

    # variables to hold overall average compound score for message
    finalScore = 0
    roundedFinalScore = 0

    # variables to hold the higest positive score is the message
    # and highest negative score in the message
    maxPosScore = 0
    maxNegScore = 0

    print("===")
    sid = SentimentIntensityAnalyzer()
    emailLines = tokenize.sent_tokenize(body)
    for line in emailLines:
        ss = sid.polarity_scores(line)
        line = line.replace('\n', ' ').replace('\r', '')
        print(line)
        for k in sorted(ss):
            print(' {0}: {1}\n'.format(k, ss[k]), end='')
        lineCompoundScore = ss['compound']
        finalScore += lineCompoundScore

        if ss['pos'] > maxPosScore:
            maxPosScore = ss['pos']
        elif ss['neg'] > maxNegScore:
            maxNegScore = ss['neg']
        
    # calculate avg compound score for the entire message
    roundedFinalScore = round(finalScore/len(emailLines), 4)
    print("***Final Email Score", roundedFinalScore)
    print("Most Positive Sentence Score: ", maxPosScore)
    print("Most Negative Sentence Score: ", maxNegScore)

    # update table with calculated fields
    try:
        updateCursor.execute(updateScoreQuery, (roundedFinalScore, maxPosScore, maxNegScore, url))
        db.commit()
    except:
        db.rollback()
db.close()
