# -*- coding:utf-8 -*-

"""
代码主要作用：练习 4.4 第 3 题
"""

import random
from ExampleCode.chapter4.node import Node
from ExampleCode.arrays import Array


def trans_array_to_link(arr:Array):
    """将数组的内容转移到链表中。"""

    length = len(arr)
    head = None
    for item in arr[::-1]:
        head = Node(item, head)

    while head != None:
        print(head.data)
        head = head.next


if __name__ == '__main__':

    arr = Array(8, 1)
    for i in range(len(arr)):
        arr[i] = random.randint(0, 10)
    print(arr)
    trans_array_to_link(arr)
