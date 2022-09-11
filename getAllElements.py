# 1305. 两个二叉搜索树中的所有元素
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    #
    #     def inorder(root):
    #         if not root:
    #             return []
    #         return inorder(root.left) + [root.val] + inorder(root.right)
    #
    #     def merge(nums1, nums2):
    #         res = []
    #         m, n = len(nums1), len(nums2)
    #         i, j = 0, 0
    #         while i < m and j < n:
    #             if nums1[i] < nums2[j]:
    #                 res.append(nums1[i])
    #                 i += 1
    #             else:
    #                 res.append(nums2[j])
    #                 j += 1
    #         if i < m:
    #             res.extend(nums1[i:])
    #         else:
    #             res.extend(nums2[j:])
    #         return res
    #
    #     return merge(inorder(root1), inorder(root2))

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        def merge(nums1, nums2):
            res = []
            m, n = len(nums1), len(nums2)
            i, j = 0, 0
            while i < m and j < n:
                if nums1[i] < nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
            if i < m:
                res.extend(nums1[i:])
            else:
                res.extend(nums2[j:])
            return res

        return merge(inorder(root1), inorder(root2))











