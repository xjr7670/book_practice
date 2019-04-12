#-*- coding:utf-8 -*-

'''
递归法实现
'''

class Dec2Bin(object):

    def __init__(self):
        self.number = 111111111111L
        self.result_list = []
    
    def get_rest(self, num):

        remainder = num % 2
        quotient = num // 2
        self.result_list.append(remainder)

        if quotient <= 1:
            self.result_list.append(quotient)
            return quotient
        else:
            return self.get_rest(quotient)
    
    def main(self):

        self.get_rest(self.number)
        for i in self.result_list[::-1]:
            print(i, end='')
        else:
            print()


if __name__ == '__main__':

    dec2bin = Dec2Bin()
    dec2bin.main()