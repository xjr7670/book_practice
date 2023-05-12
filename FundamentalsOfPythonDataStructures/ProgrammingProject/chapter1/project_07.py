# -*- coding:utf-8 -*-

import math


def median(num_list):
    """求中位数"""

    num_list.sort()
    
    length = len(num_list)
    mid = math.ceil(length / 2)

    if length % 2 == 0:
        return (num_list[mid] + num_list[mid+1]) / 2
    else:
        return num_list[mid]


def mode(num_list):
    """求众数"""

    result = {}

    for item in num_list:
        result[item] = result.get(item, 0) + 1
    
    largest = sorted(result.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    return largest[0][0]


def mean(num_list):
    """求平均值"""

    return sum(num_list) / len(num_list)


if __name__ == "__main__":
    num_list = [1, 3, 2, 3, 8, 9, 5, 7, 8, 6]
    print(median(num_list))
    print(mode(num_list))
    print(mean(num_list))