# -*- coding:utf-8 -*-

"""
代码主要作用：Defines PFEvaluatorModel and PFEvaluator
"""


from tokens import Token
from scanner import Scanner
from arraystack import ArrayStack


class PFEvaluatorModel(object):

    def evaluate(self, sourceStr):
        self._evaluator = PFEvaluator(Scanner(sourceStr))
        value = self._evaluator.evaluate()
        return value

    def format(self, sourceStr):
        normalizedStr = ''
        scanner = Scanner(sourceStr)
        while scanner.hasNext():
            normalizedStr += str(scanner.next()) + " "
        return normalizedStr;

    def evaluationStatus(self):
        return str(self._evaluator)


class PFEvaluator(object):

    def __init__(self, scanner):
        self._expressionSoFar = ''
        self._operandStack = ArrayStack()
        self._scanner = scanner

    def evaluate(self):
        while self._scanner.hasNext():
            currentToken = self._scanner.next()
            self._expressionSoFar += str(currentToken) + ' '
            if currentToken.getType() == Token.INT:
                self._operandStack.push(currentToken)
            elif currentToken.isOperator():
                if len(self._operandStack) < 2:
                    raise AttributeError('Too few operands on the stack')

                t2 = self._operandStack.pop()
                t1 = self._operandStack.pop()
                result = Token(self._computeValue(currentToken,
                                                  t1.getValue(),
                                                  t2.getValue()))
                self._operandStack.push(result)
            else:
                raise AttributeError('Unknown token type')

        if len(self._operandStack) > 1:
            raise AttributeError('Too many operands on the stack')
        result = self._operandStack.pop()
        return result.getValue()

    def __str__(self):
        result = '\n'
        if self._expressionSoFar == '':
            result += 'Portion of expression processed: none\n'
        else:
            result += 'Portion of expressoin processed: ' + \
                      self._expressionSoFar + '\n'
        if self._operandStack.isEmpty():
            result += 'The stack is empty'
        else:
            result += 'Operands on the stack: ' + str(self._operandStack)

        return result

    def _computeValue(self, op, value1, value2):
        result = 0
        theType = op.getType()
        if theType == Token.PLUS:
            result = value1 + value2
        elif theType == Token.MINUS:
            result = value1 - value2
        elif theType == Token.MUL:
            result = value1 * value2
        elif theType == Token.DIV:
            result = value1 // value2
        else:
            raise AttributeError('Unknown operator')
        return result
