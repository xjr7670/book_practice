# -*- coding:utf-8 -*-

count = 0
print("%12s%6s" % ('problem_size', 'count'))
for n in [1000, 2000, 4000, 10000, 100000]:
    problem_size = n
    while problem_size > 0:
        count += 1
        problem_size = problem_size // 2
    else:
        print('%12s%6d' % (n, count))