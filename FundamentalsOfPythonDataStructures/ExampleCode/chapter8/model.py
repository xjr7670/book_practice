# -*- coding:utf-8 -*-

"""
代码主要作用：
"""


class Condition(object):

    def __init__(self, rank):
        self._rank = rank

    def __ge__(self, other):
        """Used for comparisons."""
        return self._rank >= other._rank

    def __str__(self):
        if self._rank == 1:
            return "critical"
        elif self._rank == 2:
            return "serious"
        else:
            return "fair"


class Patient(object):

    def __init__(self, name, condition):
        self._name = name
        self._condition = condition

    def __ge__(self, other):
        """Used for comparisons."""
        return self._condition >= other._condition

    def __str__(self):
        return self._name + ' / ' + str(self._condition)
