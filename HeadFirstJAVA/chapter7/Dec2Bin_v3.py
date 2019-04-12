#-*- coding:utf-8 -*-

'''
动态规划法并利用栈结构来实现
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

        while self.result_list:
            print(self.result_list.pop(), end='')
        else:
            print()       


if __name__ == '__main__':

    dec2bin = Dec2Bin()
    dec2bin.main()