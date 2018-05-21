#-*- coding:utf-8 -*-

import feedparser
import re


feedlist=[
          'http://www.foxnews.com/xmlfeed/rss/0,4313,0,00.rss',
          'http://www.foxnews.com/xmlfeed/rss/0,4313,80,00.rss',
          'http://www.foxnews.com/xmlfeed/rss/0,4313,81,00.rss',
          ]

def stripHTML(h):
    p = ''
    s = 0
    for c in h:
        if c == '<':
            s = 1
        elif c == '>':
            s = 0
            p += ' '
        elif s == 0:
            p += c
    return p

def separatewords(text):
    spliter = re.compile('\\W*')
    return [s.lower() for s in splitter.split(text) if len(s) > 3]

def getarticlewords():
    allwords = {}
    articlewords = []
    articletitles = []
    ec = 0
    # 遍历每个订阅源
    for feed in feedlist:
        f = feedparser.parse(feed)

        # 遍历每篇文章
        for e in f.entries:
            # 跳过标题相同的文章
            if e.title in articletitles:
                continue

            # 提取单词
            txt = e.title.encode('utf8') + stripHTML(e.description.encode('utf8'))
            words = separatewords(txt)
            articlewords.append({})
            articletitles.append(e.title)

            # 在allwords和articlewords中增加针对当前单词的计数
            for word in words:
                allwords.setdefault(word, 0)
                allwords[word] += 1
                articlewords[ec].setdefault(word, 0)
                articlewords[ec][word] += 1
            ed += 1
    return allwords, articlewords, articletitles


def makematrix(allw, articlew):
    wordvec = []

    # 只考虑那些普通的但又不至于非常普通的单词
    for w, c in allw.items():
        if c > 3 and c < len(articlew) * 0.6:
            wordvec.append(w)

    # 构造单词矩阵
    l1 = [[(word in f and f[word] or 0) for word in wordvec] for f in articlew]
    return l1, wordvec
