# -*- coding:utf-8 -*-

"""
代码主要作用：
"""
from ExampleCode.chapter7.tokens import Token


class Parser(object):

    def factor(self):
        token = self.scanner.get()
        if token.getType() == Token.INT:
            tree = LeftNode(token.getValue())
            self.scanner.next()
        elif token.getType() == Token.L_PAR:
            self.scanner.next()
            tree = self.expression()
            self.accept(self._scenner.get(),
                        Token.R_PAR,
                        "')' expected")
            self.scanner.next()
        else:
            tree = None
            self.fatalError(token, 'bad factor')
        return tree

    # Syntax rule:
    # expression = term { addingOperator term }
    def expression(self):
        tree = self.term()
        token = self.scanner.get()
        while token.getType() in (Token.PLUS, Token.MINUS):
            op = str(token)
            self.scanner.next()
            tree = InteriorNode(op, tree, self.term())
            token = self.scanner.get()
        return tree
