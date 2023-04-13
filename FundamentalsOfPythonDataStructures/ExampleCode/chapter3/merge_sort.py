# -*- coding:utf-8 -*-

"""
代码主要作用：合并排序（归并排序）
"""

import random
from ExampleCode.arrays import Array


def mergeSort(lyst):
    # lyst - list being sorted
    # copyBuffer - temporary space needed during merge
    copyBuffer = Array(len(lyst))
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst) - 1)


def mergeSortHelper(lyst, copyBuffer, low, high):
    # lyst - list being sorted
    # copyBuffer - temp space needed during merge
    # low, high - bounds of sublist
    # middle - midpoint of sublist
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle + 1, high)
        merge(lyst, copyBuffer, low, middle, high)


def merge(lyst, copyBuffer, low, middle, high):
    # lyst - list that is being sorted
    # copyBufer - temp space needed during the merge process
    # low - beginning of first sorted sublist
    # middle - end of first sorted sublist
    # middle+1 beginning of second sorted sublist
    # high - end of second sorted sublist

    # Initialize i1 and i2 to the first items in each sublist
    i1 = low
    i2 = middle + 1

    # Interleave items from the sublist into the
    # copyBuffer in such a way that order is maintained
    for i in range(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        else:
            copyBuffer[i] = lyst[i2]
            i2 += 1

    for i in range(low, high + 1):
        lyst[i] = copyBuffer[i]


def main(size=20, sort=mergeSort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    print(lyst)
    sort(lyst)
    print(lyst)


if __name__ == '__main__':
    main()
