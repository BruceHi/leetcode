# 222.完全二叉树的节点个数
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 没有利用完全二叉树的性质
    # def countNodes(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # 满二叉树个数：2**n-1，n 代表层数
    def countNodes(self, root: TreeNode) -> int:

        def level(root):
            res = 0
            while root:
                res += 1
                root = root.left
            return res

        if not root:
            return 0
        left, right = level(root.left), level(root.right)
        if left == right:
            return (1 << left) + self.countNodes(root.right)
        return self.countNodes(root.left) + (1 << right)