# -*- coding:utf-8 -*-

"""
代码主要作用：Graph-processing algorithms
"""


from linkedstack import LinkedStack


def topoSort(g, startLabel=None):
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack


def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)


def spanTree(g, startLabel):
    pass


def shortestPaths(g, startLabel):
    pass
