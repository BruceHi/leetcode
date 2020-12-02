# 543. 二叉树的直径
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return max(left, right) + 1
        dfs(root)
        return res
