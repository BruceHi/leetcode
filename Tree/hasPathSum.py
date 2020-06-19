# 路径总和
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #
    #     def dfs(root, sum, level):
    #         if not level:
    #             if not root and not sum:
    #                 return False
    #
    #         if not root and not sum:  # 叶子结点
    #             return True
    #         if not root or root.val > sum:
    #             return False
    #         return dfs(root.left, sum - root.val, level + 1) \
    #             or dfs(root.right, sum - root.val, level + 1)
    #     return dfs(root, sum, 0)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # 叶子结点之后看剩余多少值。
            return sum == 0

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

