# 深度优先遍历
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 前序遍历
    # def preorderTraversal(self, root: TreeNode):
    #     if not root:
    #         return []
    #     return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    #
    # # 中序遍历
    # def inorderTraversal(self, root: TreeNode):
    #     if not root:
    #         return []
    #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    #
    # # 后序遍历
    # def postorderTraversal(self, root: TreeNode) -> list[int]:
    #     if not root:
    #         return []
    #     return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    # 迭代
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
            top = stack.pop()
            cur = top.right
        return res

    def inorderTraversal(self, root: TreeNode):
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            res.append(top.val)
            cur = top.right
        return res

    def postorderTraversal(self, root: TreeNode):
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.right
            top = stack.pop()
            cur = top.left
        return res[::-1]





