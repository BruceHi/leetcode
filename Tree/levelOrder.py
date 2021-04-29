# 层次遍历
# Definition for a binary tree node.

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#
#     #BFS(广度优先)，注意值是每一层是一个列表
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         res = []
#         queue = deque()
#         queue.append(root)
#
#         while queue:
#             level = len(queue)
#             curr = []  # 先把内层的填完了
#
#             for _ in range(level):
#                 node = queue.popleft()
#                 curr.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#
#             res.append(curr)
#
#         return res


    # DFS（深度优先），因为用到了递归（内置栈）。
    # def levelOrder(self, root: TreeNode):
    #     res = []
    #
    #     def helper(note, level):
    #         if not note:
    #             return
    #         if len(res) == level:  # 判断是否初次到了某一层。
    #             res.append([])
    #         res[level].append(note.val)
    #         helper(note.left, level+1)
    #         helper(note.right, level+1)
    #
    #     helper(root, 0)
    #     return res

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         res, queue = [], deque([root])
#
#         while queue:
#             cur = []
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 cur.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.append(cur)
#         return res

class Solution:
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #     res, queue = [], deque([root])
    #
    #     while queue:
    #         cur = []
    #         for _ in range(len(queue)):
    #             node = queue.popleft()
    #             cur.append(node.val)
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         res.append(cur)
    #     return res

    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #     queue = deque([root])
    #     res = []
    #
    #     while queue:
    #         level = []
    #         for _ in range(len(queue)):
    #             cur = queue.popleft()
    #             level.append(cur.val)
    #             if cur.left:
    #                 queue.append(cur.left)
    #             if cur.right:
    #                 queue.append(cur.right)
    #         res.append(level)
    #     return res

    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #     res = []
    #     queue = deque([root])
    #     while queue:
    #         cur = []
    #         for _ in range(len(queue)):
    #             top = queue.popleft()
    #             cur.append(top.val)
    #             if top.left:
    #                 queue.append(top.left)
    #             if top.right:
    #                 queue.append(top.right)
    #         res.append(cur)
    #     return res

    # 所有元素写在列表里面
    def levelOrder2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            # for _ in range(len(queue)):  # 可以不加外循环的
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur)
        return res



