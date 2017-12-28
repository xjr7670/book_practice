#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:23:41 2017

@author: cavin
"""

import networkx as nx
import matplotlib.pyplot as plt
import operator

g = nx.read_weighted_edgelist('data/edgelist24.csv')
degree = nx.degree(g)

# 查看网络是否都是连通的
print(nx.is_connected(g))

# 查看网络实际上有多少个子图
print(nx.number_connected_components(g))

# 打印最大的5个子图的节点数
graphs = list(nx.connected_component_subgraphs(g))
graphsSorted = sorted(graphs, key=len, reverse=True)

i = 0
for graph in graphsSorted[0:5]:
    i += 1
    print("num nodes in graph", i, ":", nx.number_of_nodes(graph))
    
    # 打印子图的度数
    graphDegree = nx.degree(graph)
    
    # draw one set with name labels
    f1 = plt.figure(figsize=(12, 8))
    degree_values = [item[1] for item in graphDegree]
    nx.draw(graph, node_size=[v * 10 for v in degree_values], with_labels=True, font_size=8)
    filename1 = 'graphLabels' + str(i) + '.png'
    f1.savefig(filename1)
    
    f2 = plt.figure(figsize=(12, 8))
    nx.draw(graph, node_size=[v * 10 for v in degree_values])
    filename2 = 'graph' + str(i) + '.png'
    f2.savefig(filename2)