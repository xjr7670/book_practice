# -*- coding:utf-8 -*-

"""
代码主要作用：链表实现的优先队列
"""


from ExampleCode.chapter4.node import Node
from linkedqueue import LinkedQueue


class LinkedPriorityQueue(LinkedQueue):
    """A link-based priority queue implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        LinkedQueue.__init__(self, sourceCollection)

    def add(self, newItem):
        """Inserts newItem after items of greater or equal
        priority or ahead of items of lesser priority.
        A has greater priority than B if A < B."""
        if self.isEmpty() or newItem >= self._rear.data:
            # New item goes at rear
            LinkedQueue.add(self, newItem)
        else:
            # Search for a position where it's less
            probe = self._front
            while newItem >= probe.data:
                trailer = probe
                probe = probe.next
            newNode = Node(newItem, probe)
            if probe == self._front:
                # New item goes at front
                self._front = newNode
            else:
                # New item goes between two nodes
                trailer.next = newNode
            self._size += 1

