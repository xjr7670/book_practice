#!/usr/bin/env python
#-*- coding:utf-8 -*-

import math
import operator


# 计算香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)                       # 获得数据集样本个数
    labelCounts = {}                                # 用来保存类别的字典
    for featVec in dataSet:                         # 循环历遍样本数据集
        currentLabel = featVec[-1]                  # 每一个样本的最后一个元素即是样本的类别
        if currentLabel not in labelCounts:
            labelCounts[currentLabel] = 0           # 类别字典以类别为键，类别出现次数为值
        labelCounts[currentLabel] += 1              # 类别加1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries # 计算每个类别出现的频率（＝类别出现的次数/样本个数）
        shannonEnt -= prob * math.log(prob, 2)      # 香农熵＝累减的 每个类别的频率*频率以2为底的对数值
    return shannonEnt


def createDataSet():
    dataSet = [
            [1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']
            ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


# 切割样本
# 传进来数据集、第几列、该列的值（根据该值来切分）
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:                         # 历遍样本每一行
        if featVec[axis] == value:                  # 判断样本中指定列是否等于指定的值
            reducedFeatVec = featVec[:axis]         # 如果是的话把样本中这一行除了指定列以外的元素
            reducedFeatVec.extend(featVec[axis+1:]) # 所组成的列表保存
            retDataSet.append(reducedFeatVec)       # 添加到返回集中
    return retDataSet


# 选择最佳特征来切割样本
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1                       # 获得样本特征个数。因为最后一个是类别，不是特征值，所以要减1
    baseEntropy = calcShannonEnt(dataSet)                   # 获得样本的香农熵
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):                            # 历遍每个特征，用来进行下一步的处理
        featList = [example[i] for example in dataSet]      # 取得样本集中每个样本的当前特征
        uniqueVals = set(featList)                          # 特征值去重
        newEntropy = 0.0
        for value in uniqueVals:                            # 对每个特征值都进行处理
            subDataSet = splitDataSet(dataSet, i, value)    # 根据特征值来切割数据集
            prob = len(subDataSet) / float(len(dataSet))    # 切割后的数据集/原始数据集，得到频率
            newEntropy += prob * calcShannonEnt(subDataSet) # 得到信息增益（＝频率*切割后的香农熵，再累加）
        infoGain = baseEntropy - newEntropy                 # 得到按照该特征切割得到的数据集的信息增益
        if infoGain > bestInfoGain:                         # 判断它是否为最大的信息增益值
            bestInfoGain = infoGain                         # 如果是的话，就把当前特征做为最佳特征值来返回
            bestFeature = i                                 # 返回的是个数字，也就是它是第几个特征
    return bestFeature


# 如果数据集已经处理了所有的特征值，
# 但是得到的类别标签依然不是唯一的，就需要用投票来解决
# 原理就是把类别字典根据值从大到小排序，然后返回最大值对应的键，就是类别了
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount:
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 创建树
# 把样本集（矩阵）转换成分类后的树
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]        # 取得类别标签列表
    if classList.count(classList[0]) == len(classList):     # 如果第一个类别出现的次数等于标签列表的长度，
        return classList[0]                                 # 说明最终数据集中只剩下一个类别了，则返回这个类别
    if len(dataSet[0]) == 1:                                # 如果数据集中每个样本长度都为1了
        return majorityCnt(classList)                       # 说明已经遍历完所有特征。返回出现次数最多的类别
    bestFeat = chooseBestFeatureToSplit(dataSet)            # 选择最佳特征值所在列数
    bestFeatLabel = labels[bestFeat]                        # 得到最佳特征值对应的类别
    myTree = {bestFeatLabel:{}}                             # 构建字典，以最佳特征类别为键，下面再保存递归得到的内容
    del(labels[bestFeat])                                   # 删除当前最佳特征值
    featValues = [example[bestFeat] for example in dataSet] # 根据最佳特征索引得到最佳特征值列表
    uniqueVals = set(featValues)                            # 去重
    for value in uniqueVals:                                # 遍历
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

    return myTree

def classify(inputTree, featLabels, testVec):
    firstStr = list(inputTree.keys())[0]            # 取得树的第一个键，即类别
    secondDict = inputTree[firstStr]                # 取得树字典的第二层内容
    featIndex = featLabels.index(firstStr)          # 得到特征的索引
    for key in secondDict.keys():                   # 根据特征值来判断
        if testVec[featIndex] == key:               # 根据最佳特征值的索引来判断测试样本
            if type(secondDict[key]).__name__ == 'dict':    # 如果返回的依然是字典，说明还需要继续判断
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]        # 否则的返回，返回对应的值
    return classLabel


def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename, 'rb')
    return pickle.load(fr)

