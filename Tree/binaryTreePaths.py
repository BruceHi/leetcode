# 257. 二叉树的所有路径
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def dfs(root, cur):
            if not root:
                return
            if not root.left and not root.right:
                res.append(cur + str(root.val))
                return
            dfs(root.left, cur + str(root.val) + '->')
            dfs(root.right, cur + str(root.val) + '->')

        dfs(root, '')
        return res
