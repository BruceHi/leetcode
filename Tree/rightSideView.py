# 199.二叉树的右视图
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def rightSideView(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     res = [root.val]
    #     queue = deque([root])
    #
    #     while queue:
    #         for _ in range(len(queue)):
    #             cur = queue.popleft()
    #             if cur.left:
    #                 queue.append(cur.left)
    #             if cur.right:
    #                 queue.append(cur.right)
    #         if queue:
    #             res.append(queue[-1].val)
    #     return res

    # def rightSideView(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     res = []
    #     queue = deque([root])   # 不能直接这么写，若是空的话 queue = deque([None]), 里面有一个值是 None 的。
    #
    #     while queue:
    #         res.append(queue[-1].val)
    #         for _ in range(len(queue)):
    #             cur = queue.popleft()
    #             if cur.left:
    #                 queue.append(cur.left)
    #             if cur.right:
    #                 queue.append(cur.right)
    #     return res

    def rightSideView(self, root: TreeNode) -> List[int]:
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
            res.append(cur[-1])
        return res
