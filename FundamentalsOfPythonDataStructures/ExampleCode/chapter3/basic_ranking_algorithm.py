# -*- coding:utf-8 -*-

"""
File basic_ranking_algorithm.py - 基本排序算法

3.4 节基本排序算法的函数集合
"""


def swap(lyst, i, j):
    """Exchange the items at positions i and j."""
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def selectionSort(lyst):
    """选择排序"""

    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1

    
def bubbleSort(lyst):
    """冒泡排序"""
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
            i += 1
        n -= 1


def bubbleSortWithTweak(lyst):
    """改进版的冒泡排序"""
    n = len(lyst)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
                swapped = True
            i += 1
        if not swapped:
            return
        n -= 1


def insertionSort(lyst):
    """插入排序"""
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i += 1