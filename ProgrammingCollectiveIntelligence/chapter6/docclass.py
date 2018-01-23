#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:03:01 2017

@author: cavin
"""

import re
import math


def getwords(doc):
    splitter = re.compile('\\W*')
    # 根据非字母字符进行单词拆分
    words = [s.lower() for x in splitter.splic(doc)
             if len(s) > 2 and len(s) < 20]
    
    # 只返回一组不重复的单词
    return dict([(w, 1) for w in words])

class classifier:
    def __init__(self, getfeatures, filename=None):
        # 统计特征/分类组合的数量
        self.fc = {}
        # 统计每个分类中的文档数量
        self.cc = {}
        self.getfeatures = getfeatures
        
    # 增加对特征/分类组合的计数值
    def incf(self, f, cat):
        self.fc.setdefault(f, {})
        self.fc[f].setdefault(cat, 0)
        self.fc[f][cat] += 1
    
    # 增加对某一分类的计数值
    def incc(self, cat):
        self.cc.setdefault(cat, )
        self.cc[cat] += 1
    
    # 某一特征出现于某一分类中的次数
    def fcount(self, f, cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0
    
    # 属于某一分类的内容项数量
    def catcount(self, cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0
    
    # 所有内容项的数量
    def totalcount(self):
        return sum(self.cc.values())
    
    # 所有分类的列表
    def categories(self):
        return self.cc.keys()
    
    # 
    def train(self, item, cat):
        features = self.getfeatures(item)
        # 针对该分类为每个特征增加计数值
        for f in features:
            self.incf(f, cat)
        
        # 增加针对该分类的计数值
        self.incc(cat)