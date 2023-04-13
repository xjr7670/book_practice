# -*- coding:utf-8 -*-


from ExampleCode.chapter10.linkedbst import LinkedBST
from ExampleCode.chapter4.abstractcollection import AbstractCollection
from abstractset import AbstractSet


class TreeSortedSet(AbstractCollection, AbstractSet):
    """A tree-based implementation of a sorted set."""

    def __init__(self, sourceCollection=None):
        self._items = LinkedBST()
        AbstractCollection.__init__(self, sourceCollection)

    def __contains__(self, item):
        """Returns True if item is in the set or False otherwise."""
        return item in self._items

    def add(self, item):
        """Adds item to the set if it is not in the set."""
        if not item in self:
            self._items.add(item)
            self._size += 1
