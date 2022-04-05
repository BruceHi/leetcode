# 深度优先遍历
from typing import List, Optional


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
    # def preorderTraversal(self, root: TreeNode) -> list[int]:
    #     res = []
    #     stack = []
    #     cur = root
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             res.append(cur.val)
    #             cur = cur.left
    #         top = stack.pop()
    #         cur = top.right
    #     return res
    #
    # def inorderTraversal(self, root: TreeNode):
    #     res = []
    #     stack = []
    #     cur = root
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         top = stack.pop()
    #         res.append(top.val)
    #         cur = top.right
    #     return res
    #
    # def postorderTraversal(self, root: TreeNode):
    #     res = []
    #     stack = []
    #     cur = root
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             res.append(cur.val)
    #             cur = cur.right
    #         top = stack.pop()
    #         cur = top.left
    #     return res[::-1]

    # 迭代
    # def preorderTraversal(self, root: TreeNode) -> list[int]:
    #     res, stack = [], []
    #     cur = root
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             res.append(cur.val)
    #             cur = cur.left
    #         top = stack.pop()
    #         cur = top.right
    #     return res


    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     res, stack = [], []
    #     cur = root
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             res.append(cur.val)
    #             cur = cur.right
    #         top = stack.pop()
    #         cur = top.left
    #     return res[::-1]



    # def inorderTraversal(self, root: TreeNode):
    #     res, stack = [], []
    #     cur = root
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         top = stack.pop()
    #         res.append(top.val)
    #         cur = top.right
    #     return res

    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     res, stack = [], []
    #     cur = root
    #     while cur and stack:
    #         while cur:
    #             stack.append(cur)
    #             res.append(cur.val)
    #             cur = cur.right
    #         top = stack.pop()
    #         cur = top.left
    #     return res[::-1]


    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     stack, res = [root], []
    #     while stack:
    #         cur = stack.pop()
    #         res.append(cur.val)
    #         if cur.left:
    #             stack.append(cur.left)
    #         if cur.right:
    #             stack.append(cur.right)
    #     return res[::-1]



    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     res, stack = [], []
    #     cur = root
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         top = stack.pop()
    #         res.append(top.val)
    #         cur = top.right
    #     return res


    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     cur, stack = root, []
    #     res = []
    #     while cur or stack:
    #         while cur:
    #             res.append(cur.val)
    #             stack.append(cur)
    #             cur = cur.left
    #         top = stack.pop()
    #         cur = top.right
    #     return res

    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     res, stack = [], []
    #     cur = root
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             res.append(cur.val)
    #             cur = cur.left
    #         top = stack.pop()
    #         cur = top.right
    #     return res


    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     stack, res = [root], []
    #     while stack:
    #         cur = stack.pop()
    #         res.append(cur.val)
    #         if cur.right:
    #             stack.append(cur.right)
    #         if cur.left:
    #             stack.append(cur.left)
    #     return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack = root, []
        res = []
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            cur = node.right
        return res


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        res, stack = [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right
        return res


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        res, stack = [], []
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            node = stack.pop()
            cur = node.left
        return res[::-1]
