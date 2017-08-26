#!/usr/bin/env python

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=5)

    plt.plot(0, 0, c='green')
    plt.plot(rw.x_values[-1], rw.y_values[-1], c='red')

    plt.axes().get_xaxis().set_visible(True)
    plt.axes().get_yaxis().set_visible(True)
    plt.show()
    
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
