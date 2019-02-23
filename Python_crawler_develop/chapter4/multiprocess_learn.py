#-*- coding:utf-8 -*-

from multiprocessing.dummy import Pool

def clac_power2(num):
    return num * num


pool = Pool(3)
origin_num = [x for x in range(10)]
result = pool.map(clac_power2, origin_num)
print(f'计算0－9的平方分别为：{result}')