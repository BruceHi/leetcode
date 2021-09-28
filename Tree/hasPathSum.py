# 112.路径总和
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     if not root:
    #         return False
    #
    #     if not root.left and not root.right:
    #         return sum == root.val
    #
    #     return self.hasPathSum(root.left, sum - root.val) \
    #         or self.hasPathSum(root.right, sum - root.val)

    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #
    #     def dfs(root, sum):
    #         if not root:
    #             return False
    #         if not root.left and not root.right:
    #             if root.val == sum:
    #                 return True
    #             return False
    #         return dfs(root.left, sum-root.val) or dfs(root.right, sum-root.val)
    #
    #     return dfs(root, sum)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum-root.val) or \
            self.hasPathSum(root.right, sum-root.val)



