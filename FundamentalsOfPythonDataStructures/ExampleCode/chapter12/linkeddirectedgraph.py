# -*- coding:utf-8 -*-

"""
代码主要作用：
"""


from ExampleCode.chapter6.abstractcollection import AbstractCollection


class LinkedDirectedGraph(AbstractCollection):

    def __init__(self, sourceCollection=None):
        """Adds a vertex with the given label to the graph."""
        self._edgeCount = 0
        self._vertices = dict()
        AbstractCollection.__init__(self, sourceCollection)

    def addVertex(self, label):
        self._vertices[label] = LinkedVertex(label)
        self._size += 1

    def removeVertex(self, label):
        """Returns True if the vertex was removed, or False otherwise."""
        removedVertex = self._vertices.pop(label, None)
        if removedVertex is None:
            return False

        # Examine all other vertices to remove edges
        # directed at the removed vertex
        for vertex in self._vertices():
            if vertex.removeEdgeTo(removedVertex):
                self._edgeCount -= 1

        # Examine all edges from the removed vertex to others
        for edge in removedVertex.incidentEdges():
            self._edgeCount -= 1

        self._size -= 1
        return True

    def addEdge(self, fromLabel, toLabel, weight):
        """Connects the vertices with an edge with the given weight."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        fromVertex.addEdgeTo(toVertex, weight)
        self._edgeCount += 1

    def getEdge(self, fromLabel, toLabel):
        """Returns the edge connecting the two vertices,
        or None if no edge exists."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        return fromVertex.getEdgeTo(toVertex)

    def removeEdge(self, fromLabel, toLabel):
        """Returns True if the edge was removed, or False otherwise."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg:
            self._edgeCount -= 1
        return edgeRemovedFlg

    def edges(self):
        """Supports iteration over the edges in the graph."""
        result = set()
        for vertex in self._vertices():
            edges = vertex.incidentEdges()
            result = result.union(set(edges))
        return iter(result)
