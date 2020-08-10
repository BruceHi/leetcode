# 相同的树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 先序遍历
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #
    #     def preorder(root):
    #         if not root:
    #             return '-'
    #         return str(root.val) + ',' + preorder(root.left) + ',' + preorder(root.right)
    #
    #     return preorder(p) == preorder(q)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
