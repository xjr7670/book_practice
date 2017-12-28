#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:03:23 2017

@author: cavin
"""

import networkx as nx

g = nx.read_weighted_edgelist('data/edgelist64.csv')
graphDegree = nx.degree(g)
pos = nx.spring_layout(g)


degree_values = [item[1] for item in graphDegree]
nx.draw(g,
        pos,
        node_size=[v * 10 for v in degree_values],
        with_labels=False,
        font_size=8)

nx.draw_networkx_nodes(g,
                       pos,
                       nodelist=['tirsen',
                                 'shen',
                                 'mlee',
                                 'ged',
                                 'objo',
                                 'stellsmi',
                                 'cowboyd',
                                 'asong',
                                 'christkv',
                                 'hisnice',
                                 'duelin_markers',
                                 'stillflame'],
                                 node_size=300,
                                 node_color='g')