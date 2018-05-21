#-*- coding:utf-8 -*-

import random
import numpy as np


def difcost(a, b):
    dif = 0
    # 遍历矩阵中的每一行和每一列
    for i in range(np.shape(a)[0]):
        for j in range(np.shape(a)[1]):
            # 将差值相加
            dif += pow(a[i, j] - b[i, j], 2)
    return dif

def factorize(v, pc=10, iter=50):
    ic = np.shape(v)[0]
    fc = np.shape(v)[1]

    # 以随机值初始化权重矩阵和特征矩阵
    w = np.matrix([[random.random() for j in range(pc)] for i in range(ic)])
    h = np.matrix([[random.random() for i in range(fc)] for i in range(pc)])

    # 最多执行iter次操作
    for i in range(iter):
        wh = w * h
        # 计算当前差值
        cost = difcost(v, wh)

        if i % 10 == 0:
            print(cost)

        # 如果矩阵已经分解彻底，则立即终止
        if cost == 0:
            break

        # 更新特征矩阵
        hn = (np.transpose(w) * v)
        hd = (np.transpose(w) * w * h)

        h = np.matrix(np.array(h) * np.array(hn) / np.array(hd))

        # 更新权重矩阵
        wn = (v * np.transpose(h))
        wd = (w * h * np.transpose(h))

        w = np.matrix(np.array(w) * np.array(wn) / np.array(wd))
    return w, h
