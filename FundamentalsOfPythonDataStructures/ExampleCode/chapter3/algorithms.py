# -*- coding:utf-8 -*-

"""
代码主要作用：Algorithms configured for profiling.
"""


def selectionSort(lyst, profiler):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            profiler.comparison()
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i, profiler)
        i += 1


def swap(lyst, i, j, profiler):
    """Exchamges the elements at positions i and j."""
    profiler.exchange()
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
