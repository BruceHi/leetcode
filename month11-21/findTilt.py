# 563. 二叉树的坡度
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def findTilt(self, root: TreeNode) -> int:
    #
    #     def change(root):
    #         if not root.left or not root.right:
    #             root.val = 0
    #         elif not root.left:
    #             root.val = change(root.right)
    #         elif not root.right:
    #             root.val = change(root.left)
    #         else:
    #             root.val = abs(change(root.left)-change(root.right))
    #         return root.val
    #
    #     change(root)

    # def findTilt(self, root: TreeNode) -> int:
    #     def root_sum(root):
    #         if not root:
    #             return 0
    #         return root.val + root_sum(root.left) + root_sum(root.right)
    #
    #     if not root:
    #         return 0
    #     now = abs(root_sum(root.left)-root_sum(root.right))
    #     return now + self.findTilt(root.left) + self.findTilt(root.right)

    def findTilt(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            sum_left = dfs(root.left)
            sum_right = dfs(root.right)
            res += abs(sum_right-sum_left)
            return root.val + sum_right + sum_left

        dfs(root)
        return res

        

