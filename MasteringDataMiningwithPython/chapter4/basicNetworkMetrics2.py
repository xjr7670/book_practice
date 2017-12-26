import networkx as nx
import matplotlib.pyplot as plt
import operator

g = nx.read_weighted_edgelist('data/edgelist24.csv')
degree = nx.degree(g)
g2 = g.copy()
d2 = nx.degree(g2)

g2_nodes = g2.nodes()
for n in g2_nodes:
    if d2[n] <= 1:
        g2.remove_nodes_from(n)

g2numNodes = nx.number_of_nodes(g2)
g2numEdges = nx.number_of_edges(g2)


print('g2numNodes: ', g2numNodes)
print('g2numEdges: ', g2numEdges)

d2_values = [item[1] for item in d2]

plt.subplot(111)
nx.draw(g2, node_size=[v * 10 for v in d2_values])
plt.show()