# 107.二叉树的层次遍历2
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = deque()
        queue = deque([root])

        while queue:
            cur = []
            for _ in range(len(queue)):
                top = queue.popleft()
                cur.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            res.appendleft(cur)
        return list(res)
