#-*- coding:utf-8 -*-

import nmf
import numpy as np
from urllib import request


tickers = ['YHOO', 'AVP', 'BIIB', 'BP', 'CL', 'CVX'
           'DNA', 'EXPE', 'GOOG', 'PG', 'XOM', 'AMGN']

shortest = 300
prices = {}
dates = None

for t in tickers:
    # 打开URL
    rows = request.urlopen('http://ichart.finance.yahoo.com/table.csv?' + 
                           's=%s&d=11&e=26&f=2006&g=d&a=3&b=12&c=1996' + 
                           '&ignore=.csv').readlines()

    # 从每一行中提取成交量
    prices[t] = [float[r.split(',')[5]) for r in rows1:] if r.strip() != '']
    if len(prices[t]) < shortest:
        shortest = len(prices[t])

    if not dates:
        dates = [r.split(',')[0] for r in rows[1:] if r.strip() != '']

l1 = [[prices[tickers[i]][j] for i in range(len(tickers))] for j in range(shortest)]

w, h = nmf.factorize(np.matrix(l1), pc=5)

print(h)
print(w)

# 遍历所有特征
for i in range(np.shape(h)[0]):
    print("Feature %d" % i)

    # 得到最符合当前特征的
    ol = [(h[i, j], tickers[j]) for j in range(np.shape(h)[])]
    ol.sort()
    ol.reverse()
    for j in range(l2):
        print(ol[j])
    print()

    # 显示最符合当前特征的交易日期
    porder = [(w[d, i], d) for d in range(300)]
    porder.sort(reverse=True)
    print([(p[0], dates[p[1]]) for p in porder[0:3]])
    print()
