# 116. 填充每个节点的下一个右侧节点指针
from collections import deque
from copy import copy


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 注意 deque 不允许被切片
    # 使用层次遍历
    # def connect(self, root: Node) -> 'Node':
    #     if not root:
    #         return root
    #     queue = deque([root])
    #     while queue:
    #         n = len(queue)
    #         for i in range(n-1):
    #             queue[i].next = queue[i+1]
    #         for _ in range(n):
    #             top = queue.popleft()
    #             if top.left:
    #                 queue.append(top.left)
    #                 queue.append(top.right)
    #     return root

    # 递归版本
    def connect(self, root: Node) -> 'Node':
        if not root or not root.left:
            return root
        root.left.next = root.right  # 两个子节点连接
        if root.next:  # 与其它节点连接
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
