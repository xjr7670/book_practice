# Python 中的实例变量

class Static(object):
    count = 4
    def __init__(self):
        count1 = 0
    
    def main(self):
        print(self.__class__.count1)

if __name__ == '__main__':

    s1 = Static()
    s1.main()

    s2 = Static()
    s2.main()