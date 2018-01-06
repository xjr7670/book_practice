#!/usr/bin/env python
#-*- coding:utf-8 -*-


import numpy as np
from sklearn.covariance import EllipticEnvelope
import matplotlib.pyplot as plt


X1 = np.loadtxt('slocbool.txt')
ee = EllipticEnvelope(support_fraction=1., contamination=0.02)
xx, yy = np.meshgrid(np.linspace(0, 1500000, 542), np.linspace(0, 15000, 542))
ee.fit(X1)
Z = ee.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(1)
plt.title("Outlier detection: SLOC vs BOOL")
plt.scatter(X1[:, 0], X1[:, 1], color='black')
plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='m')
plt.ylabel("count of boolean expressions")
plt.xlabel("count of source lines of code")
plt.show()
