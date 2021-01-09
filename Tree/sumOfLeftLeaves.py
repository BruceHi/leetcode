# 404. 左叶子之和
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 叶子之和
    # def sumOfLeftLeaves(self, root: TreeNode) -> int:
    #     # if not root:
    #     #     return 0
    #
    #
    #     res = 0
    #     def dfs(root):
    #         if not root:
    #             return
    #         nonlocal res
    #         if not root.left and not root.right:
    #             res += root.val
    #             return
    #         dfs(root.left)
    #         dfs(root.right)
    #
    #     dfs(root)
    #     return res

    # 叶子之和
    # def sumOfLeftLeaves(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     if not root.left and not root.right:
    #         return root.val
    #     return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    # flag：1 左分支，2 右分支
    # 注意：只有一个节点时，不表示叶子节点：更别提左叶子节点了
    # def sumOfLeftLeaves(self, root: TreeNode) -> int:
    #     def dfs(root, flag):
    #         if not root:
    #             return 0
    #         if not root.left and not root.right:
    #             if flag:
    #                 return root.val
    #             return 0
    #         return dfs(root.left, 1) + dfs(root.right, 0)
    #     return dfs(root, 0)

    # 早些判定左子叶点
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_node = root.left
        if left_node and not left_node.left and left_node.right:  # 判定左子叶
            return left_node.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

