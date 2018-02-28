#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os
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


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    fr.close()
    numberOfLines = len(arrayOLines)
    returnMat = np.zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


def makeScatter(datingDataMat, datingLabels):
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fmn

    myfont = fmn.FontProperties(fname='/usr/share/fonts/adobe-source-han-sans-cn/SourceHanSansCN-Regular.otf')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0 * np.array(datingLabels), 15.0 * np.array(datingLabels))
    ax.set_xlabel('每年获取的飞行常客里程数', fontproperties=myfont)
    ax.set_xlabel('玩视频游戏所耗时间百分比', fontproperties=myfont)
    #ax.set_ylabel('每周消费的冰淇淋公升数', fontproperties=myfont)
    ax.legend(True)
    plt.show()


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))


def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games? "))
    ffMiles = float(input("frequent flier miles earned per year? "))
    iceCream = float(input("liters of ice cream consumed per year? "))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = np.array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
    print("You will probably like this person: ", resultList[classifierResult - 1])


def img2vector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    fr.close()
    return returnVect


def handwritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = os.listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 2)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if classifierResult != classNumStr:
            errorCount += 1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount / float(mTest)))
