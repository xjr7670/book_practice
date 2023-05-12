# -*- coding:utf-8 -*-

"""
代码主要作用：
"""


class LinkedEdge(object):

    def __init__(self, fromVertex, toVertex, weight=None):
        self._vertex1 = fromVertex
        self._vertex2 = toVertex
        self._weight = weight
        self._mark = False

    def __eq__(self, other):
        """Two edges are equal if they connect the same vertices."""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self._vertex1 == other._vertex1 and \
            self._vertex2 == other._vertex2 and \
            self._weight == other._weight
