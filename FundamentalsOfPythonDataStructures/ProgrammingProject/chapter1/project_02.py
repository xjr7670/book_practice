# -*- coding:utf-8 -*-

def main(salary, normal_time, ot_time):
    """计算总周薪"""
    
    return salary * normal_time + salary * 1.5 * ot_time


if __name__ == "__main__":
    s = float(input("please input your salary: "))
    n = float(input("please input your normal work hour: "))
    o = float(input("please input your over time work hour: "))
    print("Yout total week salary is: %6.4f" % main(s, n, o))
