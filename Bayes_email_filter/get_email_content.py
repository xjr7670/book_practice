#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:20:24 2017

@author: cavin
"""

import re
import glob
from collections import defaultdict

class Classficator():
    
    def __init__(self):
        self.path = "/home/cavin/Downloads/email/*/*"
        
    # 得到每封邮件里面包含的所有单词
    # 单纯的数字去掉
    def tokenize(self, message):
        message = message.lower()
        all_words = re.findall("[a-z0-9']+", message)
        all_words = [w for w in all_words if not re.search(r"^\d+$", w)]
        return set(all_words)
    
    # 读取每封邮件，并获取里面所有单词
    # 统计这些词出现在垃圾邮件中和正常邮件中的频次
    # 返回一个包含所有这些单词在垃圾邮件和正常邮件中的频次的字典
    # 字典的键是这些单词，值是包含2个元素的列表
    # 第1个为出现在正常邮件中的频次，第2个为出现在垃圾邮件中的频次
    def read_files(self, path):
        counts = defaultdict(lambda: [0, 0])
        hams = 0
        spams = 0
        for fn in glob.glob(path):
            if 'ham' in fn:
                hams += 1
            if 'spam' in fn:
                spams += 1
            with open(fn, encoding="ISO-8859-1") as file:
                src = file.read()
                for word in self.tokenize(src):
                    counts[word][0 if 'ham' in fn else 1] += 1
        return (counts, hams, spams)
    
    
    # 进行贝叶斯估计
    def calc_bayes(self, word):
        counts, hams, spams = self.read_files(self.path)
        prob_a_given_b = counts[word][1] / spams
        prob_b = spams / (hams + spams)
        prob_a_given_b_bar = counts[word][0] / hams
        prob_b_bar = hams / (hams + spams)
        prob = (prob_a_given_b * prob_b) / (prob_a_given_b * prob_b + 
               prob_a_given_b_bar * prob_b_bar)
        return prob


if __name__ == "__main__":

    my_classificator = Classficator()
    sex_prob = my_classificator.calc_bayes('viagra')
    print(sex_prob)
