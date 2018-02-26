#!/usr/bin/env python
#-*- coding:utf-8 -*-


import numpy as np
import operator


def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group,labels

def classify0(inX, dataSet, labels, k):

    # 得到dataSet（矩阵）的行数
    dataSetSize = dataSet.shape[0]

    # np.tile会把inX按(dataSetSize, 1)进行重复，生成重复对象。这里生成一个与dataSet同样维度的矩阵
    # 减去dataSet，即两个矩阵相减，其实就得到了两个点的横纵坐标相减的结果。也是一个矩阵
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet

    # 矩阵的平方，即矩阵各元素分别求平方
    # 则得到两点距离计算公式中的(X1 - X0)^2
    # 结果也是矩阵
    sqDiffMat = diffMat ** 2
    # 把平方后的矩阵，按行求和
    # 则得到两点距离计算公式中的(X1 - X0)^2 + (Y1 - Y0)^2
    sqDistances = sqDiffMat.sum(axis=1)
    # 0.5次方，即1/2次方，即开平方
    distances = sqDistances ** 0.5

    # argsort是np.array对象的一个方法，它返回array对象由小到大排序后的数组索引组成的数组对象
    sortedDistIndicies = distances.argsort()

    # 下面的4行，统计前k个样本中，各个样本所属的类别出现的次数
    # 结果保存在字典中
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    # 得到的字典是以类别为键，类别出现次数为值
    # 根据字典的值（这里是类别出现次数）进行排序，逆序，即从大到小
    # 返回的是元组形式的键－值对组成的列表对象
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)

    # 返回出现次数最多的，类别
    return sortedClassCount[0][0]
