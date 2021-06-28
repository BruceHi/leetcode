# 116. 填充每个节点的下一个右侧节点指针
# 完美二叉树
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
    # def connect(self, root: Node) -> 'Node':
    #     if not root or not root.left:
    #         return root
    #     root.left.next = root.right  # 两个子节点连接
    #     if root.next:  # 与其它节点连接，连接两个支路节点
    #         root.right.next = root.next.left
    #     self.connect(root.left)
    #     self.connect(root.right)
    #     return root

    # 层次遍历，写得比较好的，没有利用完美二叉树的性质
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root:
    #         return
    #     queue = deque([root])
    #     while queue:
    #         n = len(queue)
    #         for i in range(n):
    #             node = queue.popleft()
    #             if i < n-1:  # 每一层进行连接
    #                 node.next = queue[0]
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #     return root


    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
