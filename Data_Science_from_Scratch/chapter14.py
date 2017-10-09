#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 10:19:28 2017

@author: cavin
"""

import math
import re
import random

import numpy as np

from chapter5 import mean, correlation, standard_deviation
from chapter5 import num_friends, daily_minutes, de_mean
from chapter8 import minimize_stochastic

def predict(alpha, beta, x_i):
    return beta * x_i + alpha


def error(alpha, beta, x_i, y_i):
    """the error from predicting beta * x_i + alpha
    when the actual value is y_i"""
    return y_i - predict(alpha, beta, x_i)


def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2 \
               for x_i, y_i in zip(x, y))


def least_squares_fit(x, y):
    """given training values for x and y,
    find the least-squares values of alpha and beta"""
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta


def total_sum_of_squares(y):
    """the total squared variation of y_i's from their mean"""
    return sum(v ** 2 for v in de_mean(y))


def r_squared(alpha, beta, x, y):
    """the fraction of variation in y captured by the model, which equals
    1 - the fraction of viriation in y not captured by the model"""
    
    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) / \
                  total_sum_of_squares(y))
    
    
def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2


def squared_error_gradient(x_i, y_i, theta):
    alpha, beta = theta
    return [-2 * error(alpha, beta, x_i, y_i), \
            -2 * error(alpha, beta, x_i, y_i) * x_i]




if __name__ == "__main__":
    alpha, beta = least_squares_fit(num_friends, daily_minutes)
    print(alpha, beta)
    r_squared(alpha, beta, num_friends, daily_minutes)
    random.seed(0)
    theta = [random.random(), random.random()]
    alpha, beta = minimize_stochastic(squared_error,  \
                                      squared_error_gradient, \
                                      num_friends, \
                                      daily_minutes, \
                                      theta, \
                                      0.0001)
    
    print(alpha, beta)