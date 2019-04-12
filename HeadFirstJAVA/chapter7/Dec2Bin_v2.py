#-*- coding:utf-8 -*-

'''
动态规划法实现
'''

class Dec2Bin(object):

    def __init__(self):
        self.number = 111111111111L
        self.result_list = []
    
    def get_rest(self, num):
        
        quotient = num // 2
        remainder = num % 2

        return quotient, remainder
    
    def main(self):

        quotient = self.number
        while quotient >= 1:
            quotient, remainder = self.get_rest(quotient)
            self.result_list.append(remainder)

        for i in self.result_list[::-1]:
            print(i, end='')
        else:
            print()         


if __name__ == '__main__':

    dec2bin = Dec2Bin()
    dec2bin.main()