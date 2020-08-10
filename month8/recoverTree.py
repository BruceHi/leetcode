# 恢复二叉搜索树


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def recoverTree(self, root: TreeNode) -> None:
    #
    #     def inorder(root):
    #         if not root:
    #             return []
    #         return inorder(root.left) + [root] + inorder(root.right)
    #
    #     nums = inorder(root)
    #     nums_sort = sorted(nums, key=lambda x: x.val)
    #     tmp = [nums[i] for i in range(len(nums)) if nums[i] != nums_sort[i]]
    #     tmp[0].val, tmp[1].val = tmp[1].val, tmp[0].val

    def recoverTree(self, root: TreeNode) -> None:

        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)

            return inorder(root.left) + [root] + inorder(root.right)

        nums = inorder(root)
        nums_sort = sorted(nums, key=lambda x: x.val)
        tmp = [nums[i] for i in range(len(nums)) if nums[i] != nums_sort[i]]
        tmp[0].val, tmp[1].val = tmp[1].val, tmp[0].val

