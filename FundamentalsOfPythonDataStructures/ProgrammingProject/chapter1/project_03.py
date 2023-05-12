# -*- coding:utf-8 -*-

"""
根据用户输入球的初始高度以及允许球持续弹跳的次数，返回球运动的总距离 
"""

def main():
    init_hight = float(input("init hight: "))
    dance_time = int(input("dance: "))
    
    total_distance = 0
    while dance_time > 0:
        total_distance += init_hight
        total_distance += init_hight * 0.6

        init_hight *= 0.6
        dance_time -= 1

    print("total distance is: %6.2f" % total_distance)


if __name__ == "__main__":
    main()