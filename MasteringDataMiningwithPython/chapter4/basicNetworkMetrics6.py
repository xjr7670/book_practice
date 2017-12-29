#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:13:31 2017

@author: cavin
"""

import operator
import networkx as nx

g = nx.read_weighted_edgelist('data/edgelist24.csv')

graphs = list(nx.connected_component_subgraphs(g))

conncomp = graphs[0]
ego = nx.Graph(nx.ego_graph(conncomp, 'rich', radius=3))
graphDegree = nx.degree(ego)
pos = nx.spring_layout(ego)

degree_values = [item[1] for item in graphDegree]
nx.draw(ego,
        pos,
        node_size=[v * 10 for v in degree_values],
        with_labels=True,
        font_size=8)
nx.draw_networkx_nodes(ego,
                       pos,
                       nodelist=['rich'],
                       node_size=300,
                       node_color='g')