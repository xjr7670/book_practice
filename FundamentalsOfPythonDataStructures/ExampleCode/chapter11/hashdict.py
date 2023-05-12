# -*- coding:utf-8 -*-

from abstractdict import AbstractDict, Item
from ExampleCode.chapter4.node import Node
from ExampleCode.arrays import Array


class HashDict(AbstractDict):
    """Represents a hash-based dictionary."""

    DEFAULT_CAPACITY = 9

    def __init__(self, sourceDictionary=None):
        """Will copy items to the collection from 
        sourceDictionary if it's present."""
        self._array = Array(HashDict.DEFAULT_CAPACITY)
        self._foundNode = self._priorNode = None
        self._index = -1
        AbstractDict.__init__(self, sourceDictionary)


    # Accessors
    def __contains__(self, key):
        """Returns True if key is in self or False otherwise."""
        self._index = abs(hash(key)) % len(self._array)
        self._priorNode = None
        self._foundNode = self._array[self._index]
        while self._foundNode != None:
            if self._foundNode.data.key == key:
                return True
            else:
                self._priorNode = self._foundNode
                self._foundNode = self._foundNode.next
        return False

    def __iter__(self):
        """Supports up the keys in the dictionary."""
        cursor = 0
        while cursor < len(self._array):
            yield self._array[cursor]
            cursor += 1

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raise: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        if key in self:
            return self._foundNode.data.value
        else:
            raise KeyError('Missing: ' + str(key))

    # Mutators
    def __setitem__(self, key, value):
        """If the key is in the dictionary, 
        replaces the old value with the new value.
        Otherwise, adds the key and value to it."""
        if key in self:
            self._foundNode.data.value = value
        else:
            newNode = Node(Item(key, value), self._array[self._index])
            self._array[self._index] = newNode
            self._size += 1

    def pop(self, key):
        """Removes the key and returns the associated value
        if the key is in the dictionary, or returns the default value otherwise."""
        if not key in self:
            raise KeyError('Missing: ' + str(key))
        elif self._priorNode == None:
            self._array[self._index] = self._foundNode.next
        else:
            self._priorNode.next = self._foundNode.next
        self._size -= 1
        return self._foundNode.data.value

