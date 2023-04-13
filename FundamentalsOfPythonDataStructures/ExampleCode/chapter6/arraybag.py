# -*- coding:utf-8 -*-

"""
代码主要作用：array 实现的 Bag 接口
"""

from ExampleCode.arrays import Array
from abstractbag import AbstractBag


class ArrayBag(AbstractBag):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Contructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the contents
        of sourceCollection, if it's present."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        AbstractBag.__init__(self, sourceCollection)

    # Accessor methods
    def isEmpty(self):
        """Return Thre if len(self)==0, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """-Returns the number of items in self."""
        return self._size

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        self._items[len(self)] = item
        self._size += 1

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", " .join(map(str, self)) + "}"

    def __add__(self, other):
        """Returns a new bag containing the contents of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Return True if self equals other, or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + ' not in bag')
        # Search for index of target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1

        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i+1]
        # Decrement logical size
        self._size -= 1
        # Check array memory here and decrease it if necessary


