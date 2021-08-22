# 判断是否为平衡二叉树
from functools import lru_cache

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def isBalanced(self, root: TreeNode) -> bool:
    #
    #     def depth(root):
    #         if not root:
    #             return 0
    #         return max(depth(root.left), depth(root.right)) + 1
    #
    #     def dfs(t1, t2):
    #         if not t1 and not t2:
    #             return True
    #         if t1 and not t2:
    #             return abs(depth(t1)) <= 1 and dfs(t1.left, t1.right)
    #         if t2 and not t1:
    #             return abs(depth(t2)) <= 1 and dfs(t2.left, t2.right)
    #         return abs(depth(t1) - depth(t2)) <= 1 and dfs(t1.left, t1.right) and dfs(t2.left, t2.right)
    #
    #     if not root:
    #         return True
    #     return dfs(root.left, root.right)

    # # 自顶向下
    # def isBalanced(self, root: TreeNode) -> bool:
    #
    #     def height(root):
    #         if not root:
    #             return -1
    #         return max(height(root.left), height(root.right)) + 1
    #
    #     if not root:
    #         return True
    #     return abs(height(root.left) - height(root.right)) <= 1 \
    #         and self.isBalanced(root.left) and self.isBalanced(root.right)

    # 自底向上
    # def isBalanced(self, root: TreeNode) -> bool:
    #
    #     def helper(root):
    #         if not root:
    #             return 0
    #         left = helper(root.left)
    #         right = helper(root.right)
    #         if left == -1 or right == -1 or abs(left - right) > 1:
    #             return -1  # -1 代表非平衡树
    #         return max(helper(root.left), helper(root.right)) + 1
    #
    #     return helper(root) != -1

    # def isBalanced(self, root: TreeNode) -> bool:
    #
    #     def height(root):
    #         if not root:
    #             return -1
    #         return max(height(root.left), height(root.right)) + 1
    #
    #     if not root:
    #         return True
    #     return abs(height(root.left) - height(root.right)) <= 1 \
    #         and self.isBalanced(root.left) and self.isBalanced(root.right)

    # def isBalanced(self, root: TreeNode) -> bool:
    #
    #     def height(root):
    #         if not root:
    #             return 0
    #         return 1 + max(height(root.left), height(root.right))
    #
    #     if not root:
    #         return True
    #     return abs(height(root.left) - height(root.right)) <= 1 \
    #         and self.isBalanced(root.left) and self.isBalanced(root.right)


    # -1 表示该二叉树非平衡二叉树，是人为规定的
    # def isBalanced(self, root: TreeNode) -> bool:
    #
    #     def height(root):
    #         if not root:
    #             return 0
    #         left = height(root.left)
    #         right = height(root.right)
    #         if left == -1 or right == -1 or abs(left - right) > 1:
    #             return -1
    #         return 1 + max(left, right)
    #
    #     return height(root) != -1

    # def isBalanced(self, root: TreeNode) -> bool:
    #     def depth(root):
    #         if not root:
    #             return 0
    #         return 1 + max(depth(root.left), depth(root.right))
    #
    #     if not root:
    #         return True
    #     left = depth(root.left)
    #     right = depth(root.right)
    #     if abs(left-right) > 1:
    #         return False
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)

    # def isBalanced(self, root: TreeNode) -> bool:
    #     def dfs(root):
    #         if not root:
    #             return 0
    #         left = dfs(root.left)
    #         if left == -1:
    #             return -1
    #         right = dfs(root.right)
    #         if right == -1 or abs(right-left) > 1:
    #             return -1
    #         return 1 + max(left, right)
    #     return dfs(root) != -1

    def isBalanced(self, root: TreeNode) -> bool:

        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left)-height(root.right)) <= 1 \
            and self.isBalanced(root.left) and self.isBalanced(root.right)







