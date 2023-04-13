# -*- coding:utf-8 -*-

"""
代码主要作用：
"""

from ExampleCode.chapter4.node import TwoWayNode
from ExampleCode.chapter9.abstractlist import AbstractList


class LinkedList(AbstractList):
    """A link-based list implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Uses a circular structure with a sentinel node
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head
        AbstractList.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._head.next
        while cursor != self._head:
            yield cursor.data
            cursor = cursor.next

    # Helper method returns node at position i
    def _getNode(self, i):
        """Helper method: returns a pointer to the node at position i"""
        if i == len(self):      # Constant-time access to head node
            return self._head
        if i == len(self) - 1:  # or last data node
            return self._head.previous
        probe = self._head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    # Mutator methods
    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position 1.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError('List index out of range')
        self._getNode(i).data = item

    def insert(self, i, item):
        """Insert the item at position i."""
        if i < 0:
            i = 0
        elif i > len(self):
            i = len(self)
        theNode = self._getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous.next = newNode
        theNode.previous = newNode
        self._size += 1
        self.incModCount()
