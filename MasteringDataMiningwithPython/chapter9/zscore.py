#!/usr/bin/env python
#-*- coding:utf-8 -*-


import numpy as np


with open('sloc.txt', encoding='utf-8') as f:
    data = f.readlines()
data = np.array(data, dtype=int)

amax = np.amax(data, axis=0)
print("amax: ", amax)
amin = np.amin(data, axis=0)
print("amin: ", amin)
mean = np.mean(data)
print("mean: ", mean)
median = np.median(data)
print("median: ", median)

sumsqdiff = np.sum(pow((data - median), 2))
print("sumsqdiff: ", sumsqdiff)
sqrtdiff = np.sqrt(sumsqdiff)
print("sqrtdiff: ", sqrtdiff)
mad = np.median(sqrtdiff)
print("mad: ", mad)

modzscore = (0.6745 * sumsqdiff) / mad
print("Any value higher than", modzscore, "is an outlier")
