#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np


# Apriori算法中的辅助函数
def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset, C1))        # 这里frozenset的作用是返回一个冻结的集合，冻结后集合不能再添加或删除任何元素

def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not can in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData

# Apriori算法
def aprioriGen(Lk, k):
    # create Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):                     #
        for j in range(i+1, lenLk):            # 如果前k-2个项相同时
            L1 = list(Lk[i])[:k-2]             # 将两个集合合并
            L2 = list(Lk[j])[:k-2]             #
            L1.sort()                          #
            L2.sort()                          #
            if L1 == L2:                       #
                retList.append(Lk[i] | Lk[j])  #
    return retList

def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]    # 得到包含单个元素的项集
    k = 2       # 这里的k就是项集应包含几个元素的作用，从2开始获取
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData
