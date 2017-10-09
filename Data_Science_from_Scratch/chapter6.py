#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 10:05:26 2017

@author: cavin
"""

import math
import random
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib.font_manager as fmng

plt.style.use('ggplot')
fname = "/usr/share/fonts/adobe-source-han-sans-cn/SourceHanSansCN-Regular.otf"
myfont = fmng.FontProperties(fname=fname)

def random_kid():
    return random.choice(['boy', 'girl'])


def condition_p(): 
    both_girls = 0
    older_girl = 0
    either_girl = 0
    
    random.seed(0)
    for _ in range(10000):
        younger = random_kid()
        older = random_kid()
        if older == "girl":
            older_girl += 1
        if older == "girl" and younger == "girl":
            both_girls += 1
        if older == "girl" or younger == "girl":
            either_girl += 1
            
    print("P(both | older): ", both_girls / older_girl)
    print("P(both | either): ", both_girls / either_girl)



def uniform_pdf(x):
    """概率密度函数"""
    return 1 if x >= 0 and x < 1 else 0


def uniform_cdf(x):
    """累积分布函数"""
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1
    

def normal_pdf(x, mu=0, sigma=1):
    """正太分布的概率密度函数"""
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


def normal_pdf_show():
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.figure(figsize=(8, 6))
    plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
    plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
    plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
    plt.legend()
    plt.title("多个正态分布的概率密度函数", fontproperties=myfont)
    plt.show()
    


def normal_cdf(x, mu=0, sigma=1):
    """标准正态分布的累积分布函数"""
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def normal_cdf_show():
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
    plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
    plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
    plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
    plt.legend(loc=4)
    plt.title("多个正态分布的累积分布函数", fontproperties=myfont)
    plt.show()
    


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""
    # 如果非标准型，先调整单位使之服从标准型
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z, low_p = -10.0, 0     # normal_cdf(-10)是（非常接近）0
    hi_z, hi_p = 10.0, 1        # normal_cdf(10)是（非常接近）1
    
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            # midpoint仍然太氏，搜索比它大的值
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint仍然太高，搜索比它小的值
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    
    return mid_z


def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    s = 0
    for i in range(n):
        s = s + bernoulli_trial(p)
    return s


def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]
    
    # 用条形图绘出实际的二项式样本
    histogram = Counter(data)
    plt.bar([x for x in histogram.keys()], \
            [v / num_points for v in histogram.values()], \
            0.8, \
            color='0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    
    # 用线形图绘出正态近似
    xs = list(range(min(data), max(data) + 1))
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.title("二项分布与正态近似", fontproperties=myfont)
    plt.show()
    


if __name__ == "__main__":
    condition_p()
    normal_pdf_show()
    normal_cdf_show()
    make_hist(0.75, 100, 10000)

