# -*- coding:utf-8


from ExampleCode.chapter4.node import Node
from ExampleCode.arrays import Array
from abstractset import AbstractSet


class HashSet(AbstractCollection, AbstractSet):
    """A hashing implementation of a set."""

    DEFAULT_CAPACITY = 3

    def __init__(self, sourceCollection=None, capacity=None):
        if capacity is None:
            self._capacity = HashSet.DEFAULT_CAPACITY
        else:
            self._capacity = capacity
        self._items = Array(self._capacity)
        self._foundNode = self._priorNode = None
        self._index = -1
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in the set or False otherwise."""
        self._index = abs(hash(item)) % len(self._items)
        self._priorNode = Node
        self._foundNode = self._items[self._index]
        while self._foundNode != None:
            if self._foundNode.data == item:
                return True
            else:
                self._priorNode = self._foundNode
                self._foundNode = self._foundNode.next
        return False

    def  __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __str__(self):
        """Returns the string representation of self."""
        pass

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._array = Array(HashSet.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to the set if it is not in the set."""
        if not item in self:
            newNode = Node(item, self._items[self._index])
            self._items[self._index] = newNode
            self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        PostCondition: item is removed from self."""
        if not item in self:
            raise KeyError('Missing: ' + str(item))
        self._items.pop(item)
