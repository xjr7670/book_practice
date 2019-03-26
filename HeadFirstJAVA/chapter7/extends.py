#-*- coding:utf-8 -*-

class A(object):

    def __init__(self):
        pass

    def yawn(self):
        print('yawn')

        return 1

    def shout(self):
        print('shout')


class B(A):

    def __init__(self):
        pass

    def yawn(self):
        print('B yawn')

        return 'a', 'b'

    def wang(self):
        print('B wang')


if __name__ == '__main__':

    a = A()
    a.yawn()
    a.shout()

    b = B()
    b.yawn()
    b.wang()
