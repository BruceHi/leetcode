# 剑指 offer 54. 二叉搜索树的第 k 大节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        return inorder(root)[-k]
