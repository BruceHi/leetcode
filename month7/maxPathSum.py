# 二叉树中的最大路径和
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 看得一脸懵逼，以后再看看。
    # def maxPathSum(self, root: TreeNode):
    #
    #     res = float('-inf')
    #
    #     def dfs(root):
    #         if not root:
    #             return 0
    #         left = max(0, dfs(root.left))
    #         right = max(0, dfs(root.right))
    #         nonlocal res
    #         res = max(res, root.val + left + right)
    #         return root.val + max(left, right)
    #
    #     dfs(root)
    #     return res

    def maxPathSum(self, root: TreeNode):
        res = float('-inf')

        def dfs(root):  # 返回当前节点可以获得的最大连接的和，必须要包括当前节点
            if not root:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            nonlocal res
            res = max(res, root.val + left + right)
            return root.val + max(left, right)

        dfs(root)
        return res