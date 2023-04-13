# -*- coding:utf-8 -*-

"""
代码主要作用：9.6.4 重构后的 ArrayList
"""


from ExampleCode.arrays import Array
from abstractlist import AbstractList
from arraysortedlist import ArraySortedList
from arraylistiterator import ArrayListIterator


class ArrayList(ArraySortedList):
    """An array-based list implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ArraySortedList.__init__(self, sourceCollection)

    # Accessor methods
    def index(self, item):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        return AbstractList.index(self, item)

    # Mutator methods
    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError if i is out of range."""
        if i < 0 or i >= len(self):
            raise IndexError('List index out of range')
        self._items[i] = item

    def insert(self, i, item):
        """Inserts the item at position i."""
        # Resize the array here if necesary
        if i < 0:
            i = 0
        elif i > len(self):
            i = len(self)
        if i < len(self):
            for j in range(len(self), i, -1):
                self._items[j] = self._items[j-1]
        self._items[i] = item
        self._size += 1
        self.incModCount()

    def add(self, item):
        """Adds item to self."""
        AbstractList.add(self, item)

    def listIterator(self):
        """Returns a list iterator."""
        return ArrayListIterator(self)
