# -*- coding:utf-8 -*-

"""
File: search_algorithm.py - 3.3 搜索算法
是3.3 节中各种函数的集合
"""


def indexOfMin(lyst):
    """Returns the index of the minimum item."""

    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex


def sequentialSearch(target, lyst):
    """Return the position of the target item if found,
    or -1 otherwist. """
    
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return - 1
    

def binarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1