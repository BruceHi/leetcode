# 求根到叶子节点数字之和
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 错误解法：没法定位到叶子节点。
    # def sumNumbers(self, root: TreeNode) -> int:
    #
    #     res = []
    #
    #     def dfs(root, num):
    #         if not root:
    #             res.append(num)
    #             return
    #         if root:
    #             dfs(root.left, num * 10 + root.val)
    #             dfs(root.right, num * 10 + root.val)
    #
    #     dfs(root, 0)
    #     return sum(res) // 2

    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(root, pre):
            if not root:
                return 0
            total = pre * 10 + root.val
            if not root.left and not root.right:  # 真正遍历到叶子节点
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)  # 若没有左节点或没有右节点，返回 0.

        return dfs(root, 0)
