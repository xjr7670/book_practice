# -*- coding:utf-8 -*-


def binary_search(lyst, target):
    """二分查找法"""

    left = 0
    right = len(lyst) - 1
    print('%-6s%-6s%-9s' % ('left', 'right', 'midpoint'))

    while left <= right:
        midpoint = (left + right) // 2
        print('%-6d%-6d%-9d' % (left, right, midpoint))
        if target == lyst[midpoint]:
            return midpoint
        elif target < lyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return - 1
    

if __name__ == "__main__":
    lyst = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
    print(binary_search(lyst, 44))