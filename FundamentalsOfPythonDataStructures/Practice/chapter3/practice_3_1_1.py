# -*- coding:utf-8 -*-

count = 0
print("%12s%6s" % ('problem_size', 'count'))
problem_size = 1000
while problem_size > 0:
    count += 1
    problem_size = problem_size // 2
    print('%12s%6d' % (problem_size, count))