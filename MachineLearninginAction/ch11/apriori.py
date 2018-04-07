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


# 关联规则生成函数
def generateRules(L, supportData, minConf=0.7):
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList

def calcConf(freqSet, H, supportData, br1, minConf=0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            print(freqSet-conseq, '-->', conseq, 'conf:', conf)
            br1.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmp1 = aprioriGen(H, m + 1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)

# 收集美国国会议案中action ID的函数
from time import sleep
from votesmart import votesmart
votesmart.apikey = ''
def getActionIds():
    actionIdList = []
    billTitleList = []
    fr = open('recent20bills.txt')
    for line in fr.readlines():
        billNum = int(line.split('\t')[0])
        try:
            billDetail = votesmart.votes.getBill(billNum)
            for action in billDetail.actions:
                if action.level == 'House' and \
                        (action.stage == 'Passage' or 
                                action.stage == 'Amendment Vote'):
                    actionId = int(action.actionId)
                    print('bill: %d has actionId: %d' % (billNum, actionId))
                    actionIdList.append(actionId)
                    billTitleList.append(line.strip().split('\t')[1])
        except:
            print("problem getting bill %d" % billNum)
        sleep(1)
    return actionIdList, billTitleList
