# 剑指 offer 32-3. 从上到下打印二叉树3
# 之字形打印
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #     queue = deque([root])
    #     res = []
    #
    #     while queue:
    #         i = 0
    #         cur = []
    #         for _ in range(len(queue)):
    #             node = queue.popleft()
    #             cur.append(node.val)
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         if i & 1:
    #             res.append(cur[::-1])
    #         else:
    #             res.append(cur)
    #         i += 1
    #     return res

    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #     queue = deque([root])
    #     res = []
    #
    #     # 使用 res 确定奇偶层
    #     while queue:
    #         cur = []
    #         for _ in range(len(queue)):
    #             node = queue.popleft()
    #             cur.append(node.val)
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         res.append(cur[::-1] if len(res) & 1 else cur)
    #     return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        i = 0
        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if i & 1:
                cur.reverse()
            res.append(cur)
            i += 1
        return res

