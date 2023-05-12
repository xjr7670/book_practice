# -*- coding:utf-8 -*-

"""
Author: Cavin Xian
根据输入的球体半径计算球的直径、圆周长、表面积和体积
"""

import math


def main():
    """输入球体半径
    返回球体的直径、圆周长、表面积和体积"""

    radius = float(input("Please input the radius: "))
    diameter = radius * 2
    circumference = math.pi * 2 * radius
    surface_area = math.pi * 4 * radius * radius
    v = 3 / 4 * math.pi * math.pow(radius, 3)

    print("球的直径是：", diameter)
    print("球的圆周长是：%6.4f" % circumference)
    print("球的表面积是：%6.4f" % surface_area)
    print("球的体积是：%6.4f" % v)


if __name__ == '__main__':

    main()
    