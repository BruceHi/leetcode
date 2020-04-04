# 二叉树的深度（指的就是最大深度）和最小深度


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def minDepth(self, root: TreeNode):
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        # 不能如下的写法，如果没有左子树或右子树，深度就是 0+1了，这不太可能。
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
