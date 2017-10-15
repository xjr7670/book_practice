#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:58:32 2017

@author: cavin
"""

import math
import random

from collections import Counter, defaultdict
from functools import partial

from chapter13 import tokenize

def word_count_old(documents):
    """word count not using MapReduce"""
    return Counter(word for document in documents for word in tokenize(document))

def wc_mapper(document):
    """for each word in the document, emit (word, 1)"""
    for word in tokenize(document):
        yield (word, 1)

def wc_reducer(word, counts):
    """sum up the counts for a word"""
    yield (word, sum(counts))

def word_count(documents):
    """count the words in the input documents using MapReduce"""
    
    # 存放分好组的值
    collector = defaultdict(list)
    
    for document in documents:
        for word, count in wc_mapper(document):
            collector[word].append(count)
    
    return [output for word, counts in collector.items() \
            for output in wc_reducer(word, counts)]
    
def map_reduce(inputs, mapper, reducer):
    """runs MapReduce on the inputs using mapper and reducer"""
    collector = defaultdict(list)
    
    for input in inputs:
        for key, value in mapper(input):
            collector[key].append(value)
    
    return [output \
            for key, values in collector.items() \
            for output in reducer(key, values)]

word_counts = map_reduce(documents, wc_mapper, wc_reducer)

def reduce_values_using(aggregation_fn, key, values):
    """reduces a key-values pair by applying aggregation_fn to the values"""
    yield (key, aggregation_fn(values))

def values_reducer(aggregation_fn):
    """turns a function (values -> output) into a reducer
    that maps (key, values) -> (key, output)"""
    return partial(reduce_values_using, aggregation_fn)

sum_reducer = values_reducer(sum)
max_reducer = values_reducer(max)
min_reducer = values_reducer(min)
count_distinct_reducer = values_reducer(lambda values: len(set(values)))

def data_science_day_mapper(status_update):
    """yields (day_of_week, 1) if status_update contains "data science" """
    if "data science" in status_update['text'].lower():
        day_of_week = status_update['created_at'].weekday()
        yield (day_of_weed, 1)

data_science_days = map_reduce(status_updates, data_science_day_mapper, sum_reducer)

def words_per_user_mapper(status_update):
    user = status_update["username"]
    for word in tokenize(status_update['text']):
        yield (user, (word, 1))

def most_popular_word_reducer(user, words_and_counts):
    """given a sequence of (word, count) pairs,
    return the word with the highest total count"""
    
    word_counts = Counter()
    for word, count in words_and_counts:
        word_counts[word] += count
    
    word, count = word_counts.most_common(1)[0]
    
    yield (user, (word, count))

user_words = map_reduce(status_updates, words_per_user_mapper, \
                        most_popular_word_reducer)

def liker_mapper(status_update):
    user = status_update['username']
    for liker in  status_update['liked_by']:
        yield (user, liker)
    
distinct_likers_per_user = map_reduce(status_updates, liker_mapper, count_distinct_reducer)

def matrix_multiply_mapper(m, element):
    """ m is the common dimension (columns of A, rows of B)
    element is a tuple (matrix_name, i, j, value)"""
    name, i, j, value = element
    
    if name == "A":
        # A_ij是每个C_ik之和的第j个元素，其中k=1..m
        for k in range(m):
            # 与C_ik的其他元素分组
            yield ((i, k), (j, value))
    else:
        # B_ij是每个C_kj之和的第i个元素
        for k in range(m):
            # 与C_kj的其他元素分组
            yield ((k, j), (i, value))

def matrix_multiply_reducer(m, key, indexed_values):
    results_by_index = defaultdict(list)
    for index, value in indexed_values:
        results_by_index[index].append(value)
    
    # 对有两个结果的位置把所有的乘积加起来
    sum_product = sum(results[0] * results[1] \
                      for results in results_by_index.values())
    
    if sum_product != 0.0:
        yield (key, sum_product)