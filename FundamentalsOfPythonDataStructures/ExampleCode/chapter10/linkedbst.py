# -*- coding:utf-8 -*-

"""
代码主要作用：
"""

from ExampleCode.chapter6.abstractcollection import AbstractCollection
from bstnode import BSTNode


class LinkedBST(AbstractCollection):
    """"A link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the contents of
        sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(sourceCollection)

    def find(self, item):
        """Returns data if item is found or None otherwise."""

        # Helper function to search the binary tree
        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        # Top-level call on the root node
        return recurse(self._root)

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)

    def __str__(self):
        """Returns a string representation with the tree
        rotated 90 degrees counterclockwise."""

        def recurse(node, level):
            s = ''
            if node != None:
                s += recurse(node.right, level+1)
                s += '| ' * level
                s += str(node.data) + '\n'
                s += recurse(node.left, level+1)
            return s
        return recurse(self._root, 0)

    def add(self, item):
        """Adds item to the tree"""

        # Helper function to search for item's position
        def recurse(node):
            # New item is less; go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left == BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal;
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
            # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1
