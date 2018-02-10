#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 12:00:21 2018

@author: cavin
"""

import numpy as np
import matplotlib.pyplot as plt

X_train = np.array([
     [158, 64],
     [170, 86],
     [183, 84],
     [191, 80],
     [155, 49],
     [163, 59],
     [180, 67],
     [158, 54],
     [170, 67]
     ])
y_train = ['male', 'male', 'male', 'male', 'female', 'female', 
           'female', 'female', 'female']

plt.figure()
plt.title("Human Heights and Weights by Sex")
plt.xlabel("Height in cm")
plt.ylabel("Weight in kg")

for i, x in enumerate(X_train):
    plt.scatter(x[0], x[1], c='k', marker='x' if y_train[i] == 'male' else 'D')
plt.grid(True)
plt.show()