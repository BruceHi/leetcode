# 层次遍历
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # BFS(广度优先)
    # def levelOrder(self, root: TreeNode):
    #     if not root:
    #         return []
    #     res = []
    #     queue = deque()
    #     queue.append(root)
    #
    #     while queue:
    #         level = len(queue)
    #         curr = []  # 先把内层的填完了
    #
    #         for _ in range(level):
    #             node = queue.popleft()
    #             curr.append(node.val)
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #
    #         res.append(curr)
    #     return res

    # DFS（深度优先），因为用到了递归（内置栈）。
    def levelOrder(self, root: TreeNode):
        res = []

        def helper(note, level):
            if not note:
                return
            if len(res) == level:  # 判断是否初次到了某一层。
                res.append([])
            res[level].append(note.val)
            helper(note.left, level+1)
            helper(note.right, level+1)

        helper(root, 0)
        return res
