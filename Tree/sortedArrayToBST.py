# 将有序数组转换为二叉搜索树
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def sortedArrayToBST(self, nums):
    #     if not nums:
    #         return
    #     mid = len(nums) // 2
    #     root = TreeNode(nums[mid])
    #     if mid == 0:  # 叶结点
    #         return root
    #     root.left = self.sortedArrayToBST(nums[:mid])
    #     root.right = self.sortedArrayToBST(nums[mid+1:])
    #     return root

    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     if not nums:
    #         return
    #     mid = len(nums) >> 1
    #     node = TreeNode(nums[mid])
    #     if not mid:
    #         return node
    #     node.left = self.sortedArrayToBST(nums[:mid])
    #     node.right = self.sortedArrayToBST(nums[mid+1:])
    #     return node

    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     if not nums:
    #         return
    #     mid = len(nums) >> 1
    #     root = TreeNode(nums[mid])
    #     root.left = self.sortedArrayToBST(nums[:mid])
    #     root.right = self.sortedArrayToBST(nums[mid+1:])
    #     return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
