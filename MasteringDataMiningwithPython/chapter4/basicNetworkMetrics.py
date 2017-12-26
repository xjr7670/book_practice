import networkx as nx
import matplotlib.pyplot as plt
import operator

g = nx.read_weighted_edgelist('data/edgelist24.csv')
degree = nx.degree(g)

numNodes = nx.number_of_nodes(g)
numEdges = nx.number_of_edges(g)
minDegree = min([item[1] for item in degree])
maxDegree = max([item[1] for item in degree])


print('numNodes: ', numNodes)
print('numEdges: ', numEdges)
print('minDegree: ', minDegree)
print('maxDegree: ', maxDegree)

degreeSorted = sorted(degree, key=operator.itemgetter(1), reverse=True)
print(degreeSorted[0:9])

plt.subplot(111)
nx.draw(g)
plt.show()