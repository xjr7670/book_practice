# -*- coding:utf-8 -*-

"""
代码主要作用：
"""


class LeafNode(object):
    """Represents an integer."""

    def __init__(self, data):
        self._data = data

    def postfix(self):
        return str(self)

    def __str__(self):
        return str(self._data)
