#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 09:32:12 2017

@author: cavin
"""

import re
import glob
import math
import random
from collections import Counter, defaultdict


def tokenize(message):
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", message)
    return set(all_words)


def count_words(training_set):
    """training set consists of pairs (message, is_spam)"""
    counts = defaultdict(lambda: [0, 0])
    for message, is_spam in training_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1] += 1
    return counts


def word_probabilities(counts, total_spams, total_non_spams, k=0.5):
    """turn the word_counts into a list of triplets
    w, p(w | spam) and p(w | ~spam)"""
    return [(w, \
             (spam + k) / (total_spams + 2 * k), \
             (non_spam + k) / (total_spams + 2 * k)) \
             for w, (spam, non_spam) in counts.items()]


def spam_probability(word_probs, message):
    message_words = tokenize(message)
    log_prob_if_spam = log_prob_if_not_spam = 0.0
    
    # 迭代词汇表中每一个单词
    for word, prob_if_spam, prob_if_not_spam in word_probs:

        if word in message_words:
            # 如果*word*出现在了邮件中
            # 则增加看到它的对数概率
            log_prob_if_spam += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)
        else:
            # 如果*word*没有出现在邮件中
            # 则增加看不到它的对数概率
            # 也就是log(1 - 看到它的概率)
            log_prob_if_spam += math.log(1.0 - prob_if_spam)
            log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)
    
    prob_if_spam = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)


class NaiveBayesClassifier:

    def __init__(self, k=0.5):
        self.k = k
        self.word_probs = []
    
    def train(self, training_set):
        
        # 对垃圾邮件和非垃圾邮件计数
        num_spams = len([is_spam for message, is_spam in training_set if is_spam])
        num_non_spams = len(training_set) - num_spams
        
        # 通过"pipeline"运行训练数据
        word_counts = count_words(training_set)
        self.word_probs = word_probabilities(word_counts, num_spams, num_non_spams, self.k)
        
    def classify(self, message):
        return spam_probability(self.word_probs, message)

def test_model():
    """测试模型"""
    path = r"/home/cavin/Code/Python/Data_Science_from_Scratch/"
    data = []
    
    # grob.glob会返回每一个与通配路径所匹配的文件名
    for fn in glob.glob(path):
        is_spam = "ham" not in fn
        
        with open(fn, 'r') as file:
            for line in file:
                if line.startswith("Subject"):
                    # 移除开头的"Subject:"，保留其余内容
                    subject = re.sub(r"^Subject: ", "", line).strip()
                    data.append((subject, is_spam))
    
    random.seed(0)
    train_data, test_data = split_data(data, 0.75)
    
    classifier = NaiveBayesClassifier()
    classifier.train(train_data)
    
    # 三个元素（主题，确实是垃圾邮件，预测为垃圾邮件的概率
    classified = [(subject, is_spam, classifier.classify(subject)) \
                  for subject, is_spam in test_data]
    
    # 假设spam_probability > 0.5对应的预测为垃圾邮件
    # 对(actual is_spam, predicted is_spam)的组合计数
    counts = Counter((is_spam, spam_probability > 0.5) \
                     for _, is_spam, spam_probability in classified)
    
    # 根据spam_probability从最小到最大排序
    classified.sort(key=lambda row: row[2])
    
    # 非垃圾邮件被预测为垃圾邮件的最高概率
    spammiest_hams = filter(lambda row: not row[1], classified)[-5:]
    
    # 垃圾邮件被预测为垃圾邮件的最低概率
    hammiest_spams = filter(lambda row: row[1], classified)[:5]
    

def p_spam_given_word(word_prob):
    """use bayes's theorem to compute p(spam | message contains word)"""
    # word_prob是由word_probabilities生成的三元素中的一个
    word, prob_if_spam, prob_if_not_spam = word_prob
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)

words = sorted(test_model.classifier.word_probs, key=p_spam_given_word)
spammiest_words = words[-5:]
hammiest_words = words[:5]
    