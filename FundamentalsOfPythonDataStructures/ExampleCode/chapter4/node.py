# -*- coding:utf-8 -*-

"""
代码主要作用：
"""

class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next=None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next


class TwoWayNode(Node):

    def __init__(self, data, previous=None, next=None):
        """Instantiates a TwoWayNode."""
        Node.__init__(self, data, next)
        self.previous = previous
