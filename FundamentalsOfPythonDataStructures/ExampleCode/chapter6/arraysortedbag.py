# -*- coding:utf-8 -*-

"""
代码主要作用：array 实现的 Bag 接口
"""

from ExampleCode.chapter5.arraybag import ArrayBag


class ArraySortedBag(ArrayBag):
    """An array-based sorted bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Contructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present"""
        ArrayBag.__init__(self, sourceCollection)

    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise."""
        left = 0
        right = len(self) - 1
        while left <= right:
            midPoint = (left + right) // 2
            if self._items[midPoint] == item:
                return True
            elif self._items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        return False

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
        self._items = ArraySortedBag(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Empty or last item, call ArrayBag.add
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            ArrayBag.add(self, item)
        else:
            # Resize the array if it is full here
            # Search for first item >= new item
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            # Open a hole for new item
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i-1]
            # Insert item and update size
            self._items[targetIndex] = item
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
        flag = True
        if not self is other:
            flag = False
        if type(self) != type(other) or len(self) != len(other):
            flag = False

        for i in range(len(self)-1):
            if self._items[i] != other[i]:
                flag = False
                break
        return flag

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


