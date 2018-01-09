#!/usr/bin/env python
#-*- coding:utf-8 -*-


my_data = [['slashdot', 'USA', 'yes', 18, 'None'],
          ['google', 'France', 'yes', 23, 'Premium'],
          ['digg', 'USA', 'yes', 24, 'Basic'],
          ['kiwitobes', 'France', 'yes', 23, 'Basic'],
          ['google', 'UK', 'no', 21, 'Premium'],
          ['(direct)', 'New Zealand', 'no', 12, 'None'],
          ['(direct)', 'UK', 'no', 24, 'Basic'],
          ['google', 'USA', 'no', 24, 'Premium'],
          ['slashot','France', 'yes', 19, 'None'],
          ['digg', 'USA', 'no', 18, 'None'],
          ['google', 'UK', 'no', 18, 'None'],
          ['kiwitobes', 'UK', 'no', 19, 'None'],
          ['digg', 'New Zealand', 'yes', 12, 'Basic'],
          ['google', 'UK', 'yes', '18', 'Basic'],
          ['kiwitobes', 'France', 'yes', 19, 'Basic']]

class decisionnode:
    
    def __init__(self, col=-1, value=None, results=None, tb=None, fb=None):
        self.col = col
        self.value = value
        self.results = results
        self.tb = tb
        self.fb = fb


# 在某一列上对数据集合进行拆分，能够处理数值型数据或名词性数据
def divideset(rows, column, value):
    # 定义一个函数，令其告诉我们数据行属于第一组（返回值为true）还是第二组（返回值为false）
    split_function = None
    if isinstance(value, int) or isinstance(value, float):
        split_function = lambda row: row[column] >= value
    else:
        split_function = lambda row: row[column] == value

    # 将数据集拆分成两个集合，并返回
    set1 = [row for row in rows if split_function(row)]
    set2 = [row for row in rows if not split_function(row)]
    return (set1, set2)


# 对各种可能的结果进行计数（每一行数据的最后一列记录了这一计数结果）
def uniquecounts(rows):
    results = {}
    for row in rows:
        # 计数结果在最后一列
        r = row[len(row) - 1]
        if r not in results:
            results[r] = 0
        results[r] += 1
    return results


# 随机放置的数据项出现于错误分类中的概率
def giniimpurity(rows):
    total = len(rows)
    counts = uniquecounts(rows)
    imp = 0

    for k1 in counts:
        p1 = float(counts[k1]) / total
        for k2 in counts:
            if k1 == k2:
                continue
            p2 = float(counts[k2]) / total
            imp += p1 * p2

    return imp


# 熵是遍历所有可能的结果之后所得到的p(x)log(p(x))之和
def entropy(rows):
    from math import log
    log2 = lambda x: log(x) / log(2)
    results = uniquecounts(rows)
    # 此处开始计算熵的值
    ent = 0.0
    for r in results.keys():
        p = float(results[r]) / len(rows)
        ent = ent - p * log2(p)

    return ent
