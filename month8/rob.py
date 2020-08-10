# 打家劫舍
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def rob(self, root: TreeNode) -> int:
    #     f, g = defaultdict(int), defaultdict(int)
    #
    #     def dfs(root):
    #         if not root:
    #             return
    #         dfs(root.left)
    #         dfs(root.right)
    #         f[root] = root.val + g[root.left] + g[root.right]
    #         g[root] = max(f[root.left], g[root.left]) + max(f[root.right], g[root.right])
    #
    #     dfs(root)
    #     return max(f[root], g[root])

    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            left_rob, left_not = dfs(root.left)
            right_rob, right_not = dfs(root.right)
            return root.val + left_not + right_not, \
                max(left_rob, left_not) + max(right_rob, right_not)

        return max(dfs(root))
