# 653. 两数之和 IV - 输入 BST
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    #     def preorder(root):
    #         if not root:
    #             return []
    #         return [root.val] + preorder(root.left) + preorder(root.right)
    #
    #     nums = set(preorder(root))
    #     for num in nums:
    #         # num * 2 != k ：杜绝出现 3 + 3 = 6 类似的，因为二叉搜索树所以数字都是唯一的。
    #         if num * 2 != k and k - num in nums:
    #             return True
    #     return False

    # def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    #     def preorder(root):
    #         if not root:
    #             return []
    #         return [root.val] + preorder(root.left) + preorder(root.right)
    #
    #     nums = set(preorder(root))
    #     for num in nums:
    #         # num * 2 != k ：杜绝出现 3 + 3 = 6 类似的，因为二叉搜索树所以数字都是唯一的。
    #         if num * 2 != k and k - num in nums:
    #             return True
    #     return False


    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        record = set()

        def dfs(root):
            if not root:
                return False
            if k - root.val in record:
                return True
            record.add(root.val)
            return dfs(root.left) or dfs(root.right)

        return dfs(root)
