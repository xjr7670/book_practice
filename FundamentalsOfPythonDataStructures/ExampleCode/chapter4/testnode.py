# -*- coding:utf-8 -*-

"""
代码主要作用：测试 Node 类
"""

from node import Node


head = None

# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = Node(count, head)

# Print the contents of th structure
while head != None:
    print(head.data)
    head = head.next

