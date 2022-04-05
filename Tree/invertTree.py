# 226. 翻转二叉树
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if not root:
    #         return
    #     if not root.left and not root.right:
    #         return root
    #     tmp1, tmp2 = root.left, root.right
    #     root.left = self.invertTree(tmp2)
    #     root.right = self.invertTree(tmp1)
    #     return root

    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if not root:
    #         return
    #     # 不能拆开，否则起不到交换的目的了。
    #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #     return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
