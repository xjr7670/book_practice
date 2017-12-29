#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 20:18:31 2017

@author: cavin
"""

import networkx as nx

g = nx.read_weighted_edgelist('data/edgelist24.csv')
graphs = list(nx.connected_component_subgraphs(g))

for graph in graphs:
    if graph.has_node('rich'):
        ego = nx.Graph(nx.ego_graph(graph, 'rich', radius=2))
        graphDegree = nx.degree(ego)
        degree_values = [item[1] for item in graphDegree]
        pos = nx.spring_layout(graph)
        nx.draw(graph,
                pos,
                node_size=[v * 10 for v in degree_values],
                with_labels=False,
                font_size=8)
        nx.draw_networkx_nodes(graph,
                               pos,
                               nodelist=['rich'],
                               node_size=300,
                               node_color='g')