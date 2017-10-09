#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:45:44 2017

@author: cavin
"""

import math
import random
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib.font_manager as fmng

from chapter6 import normal_cdf
from chapter6 import inverse_normal_cdf

fname = "/usr/share/fonts/adobe-source-han-sans-cn/SourceHanSansCN-Regular.otf"
myfont = fmng.FontProperties(fname=fname)


def normal_approximation_to_binomial(n, p):
    """finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


# 正态cdf是一个变量在一个阈值以下的概率
normal_probability_below = normal_cdf

# 如果它不在阈值以下，就在阈值以上
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# 如果它小于hi但不比lo小，那么它在区间之内
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# 如果不在区间之内，就在区间之外
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2
    
    # 上界应有在它之上的tail_probability
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    
    # 下界应有在它之下的tail_probability
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    
    return lower_bound, upper_bound

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # 如果x大于均值，tail表示比x大多少
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # 如果x比均值小，tail表示比x小多少
        return 2 * normal_probability_below(x, mu, sigma)


def run_experiment():
    """flip a fair coin 1000 times, True = heads, False = tails"""
    return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment):
    """using the 5% significance levels"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531


def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma


def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

def B(alpha, beta):
    """a normalizing constant so that the total probability is 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)



if __name__ == "__main__":
    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
    print(normal_two_sided_bounds(0.95, mu_0, sigma_0))
    
    # 基于假设是0.5时95％的边界
    lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
    
    # 基于p = 0.55的真实mu和sigma
    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
    
    # 第2类错误意味着我们没有拒绝原假设
    # 这会在X仍然在最初的区间时发生
    type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
    power = 1 - type_2_probability
    print(power)
    
    hi = normal_upper_bound(0.95, mu_0, sigma_0)
    print(hi)

    type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
    power = 1 - type_2_probability
    print(power)

    print(two_sided_p_value(529.5, mu_0, sigma_0))


#    extreme_value_count = 0
#    for _ in range(100000):
#        num_heads = sum(1 if random.random() < 0.5 else 0 for _ in range(1000))
#        if num_heads >= 530 or num_heads <= 470:
#            extreme_value_count += 1
#            
#    print(extreme_value_count / 100000)

    print(two_sided_p_value(531.5, mu_0, sigma_0))
    
    upper_p_value = normal_probability_above
    lower_p_value = normal_probability_below
    
    print(upper_p_value(524.5, mu_0, sigma_0))
    print(upper_p_value(526.5, mu_0, sigma_0))


    random.seed(0)
    experiments = [run_experiment() for _ in range(1000)]
    num_rejections = len([experiment for experiment in experiments \
                          if reject_fairness(experiment)])
    print(num_rejections)

    z = a_b_test_statistic(1000, 200, 1000, 180)
    print(z)
    print(two_sided_p_value(z))
    z = a_b_test_statistic(1000, 200, 1000, 150)
    print(z)
    print(two_sided_p_value(z))




















