# -*- coding:utf-8 -*-

"""
代码主要作用：
"""

from linkededge import LinkedEdge


class LinkedVertex(object):

    def __init__(self, label):
        self._label = label
        self._edgeList = list()
        self._mark = False

    def setLabel(self, label, g):
        """Sets the vertex's lable to label."""
        g._vertices.pop(self._label, None)
        g._vertices[label] = self
        self._label = label

    def neightboringVertices(self):
        """Returns the neighboring vertices of this vertex."""
        vertices = list()
        for edge in self._edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)

    def removeEdgeTo(self, toVertex):
        """Returns True if the edge exists and is removed,
        or False otherwise."""
        edge = LinkedEdge(self, toVertex)
        if edge in self._edgeList:
            self._edgeList.remove(edge)
            return True
        else:
            return False