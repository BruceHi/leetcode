# 103. 二叉树的锯齿性层次遍历
# 二叉树的层次遍历的变形
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    # def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #     queue, res = deque([root]), []
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
    #     # return [x for x in ]
    #     for i in range(len(res)):
    #         if i & 1:
    #             res[i].reverse()
    #     return res

    # def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #     queue, res = deque([root]), []
    #     level = 0
    #
    #     while queue:
    #         tmp = []
    #         for _ in range(len(queue)):
    #             cur = queue.popleft()
    #             tmp.append(cur.val)
    #             if cur.left:
    #                 queue.append(cur.left)
    #             if cur.right:
    #                 queue.append(cur.right)
    #         if level & 1:
    #             res.append(list(reversed(tmp)))
    #         else:
    #             res.append(tmp)
    #         level += 1
    #
    #     return res

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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
            if len(res) & 1:
                res.append(cur[::-1])
            else:
                res.append(cur)
        return res














