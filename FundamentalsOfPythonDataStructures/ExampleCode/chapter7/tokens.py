# -*- coding:utf-8 -*-

"""
代码主要作用：Tokens for processing expressions.
"""


class Token(object):
    UNKNOWN = 0
    INT = 4
    MINUS = 5
    PLUS = 6
    MUL = 7
    DIV = 8
    FIRST_OP = 5

    def __init__(self, value):
        if type(value) == int:
            self._type = Token.INT
        else:
            self._type = self._makeType(value)
        self._value = value

    def isOperator(self):
        return self._type >= Token.FIRST_OP

    def __str__(self):
        return str(self._value)

    def getType(self):
        return self._type

    def getValue(self):
        return self._value

    def _makeType(self, ch):
        if ch == '*':
            return Token.MUL
        elif ch == '/':
            return Token.DIV
        elif ch == '+':
            return Token.PLUS
        elif ch == '-':
            return Token.MINUS
        else:
            return Token.UNKNOWN
