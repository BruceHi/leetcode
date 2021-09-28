# 113.路径总和2
# 找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    #     res = []
    #
    #     def dfs(root, sum, cur):
    #         if not root:
    #             return
    #         if not root.left and not root.right:  # 叶子节点
    #             if root.val == sum:
    #                 res.append(cur+[sum])
    #             return
    #         dfs(root.left, sum - root.val, cur + [root.val])
    #         dfs(root.right, sum - root.val, cur + [root.val])
    #
    #     dfs(root, sum, [])
    #     return res


    # def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
    #     res = []
    #
    #     def path(root, target, cur):
    #         if not root:
    #             return
    #         if not root.left and not root.right:
    #             if root.val == target:
    #                 res.append(cur+[target])
    #             return
    #         path(root.left, target-root.val, cur+[root.val])
    #         path(root.right, target-root.val, cur+[root.val])
    #
    #     path(root, target, [])
    #     return res

    # def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
    #     res = []
    #
    #     def path(root, cur, target):
    #         if not root:
    #             return
    #         if not root.left and not root.right:
    #             if root.val == target:
    #                 res.append(cur+[target])
    #             return
    #         path(root.left, cur+[root.val], target-root.val)
    #         path(root.right, cur+[root.val], target-root.val)
    #
    #     path(root, [], target)
    #     return res

    def pathSum(self, root, targetSum: int) -> List[List[int]]:
        res = []

        def dfs(root, cur, targetSum):
            if not root:
                return
            if not root.left and not root.right:
                if root.val == targetSum:
                    res.append(cur+[root.val])
                return
            dfs(root.left, cur+[root.val], targetSum-root.val)
            dfs(root.right, cur+[root.val], targetSum-root.val)

        dfs(root, [], targetSum)
        return res
