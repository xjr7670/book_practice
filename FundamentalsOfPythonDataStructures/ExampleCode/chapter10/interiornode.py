# -*- coding:utf-8 -*-

"""
代码主要作用：
"""


class InteriorNode(object):
    """Represents an operator and its two operands."""

    def __init__(self, op, leftOper, rightOper):
        self._operator = op
        self._leftOperand = leftOper
        self._rightOperand = rightOper

    def postfix(self):
        return self._leftOperand.postfix() + ' ' + \
            self._rightOperand.postfix() + ' ' + \
            self._operator
