#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:53:45 2017

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
    
    # 子图的度数
    graphDegree = nx.degree(graph)
    
    # find cliques
    cliques = list(nx.find_cliques(graph))
    print('cliques for graph' + str(i))
    print(cliques)
    
    # calculate eigenvector centrality
    ev = nx.eigenvector_centrality_numpy(graph)
    evSorted = sorted(ev.items(), key=operator.itemgetter(1), reverse=True)
    for key, val in evSorted:
        print(key, str(round(val, 2)))