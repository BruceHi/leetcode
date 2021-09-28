# 437.路径总和3
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # # 双重dfs，正确
    # def pathSum(self, root: TreeNode, sum: int) -> int:
    #     res = 0
    #
    #     def search(root, target):  # 只是搜索根节点到向下节点等于定值的路径总数。
    #         nonlocal res
    #         if not root:
    #             return
    #         if root.val == target:
    #             res += 1
    #         search(root.left, target-root.val)
    #         search(root.right, target-root.val)
    #
    #     def dfs(root):
    #         if not root:
    #             return
    #         search(root, sum)
    #         dfs(root.left)
    #         dfs(root.right)
    #
    #     dfs(root)
    #     return res


    # dfs，这个其实也用到了前缀和，但和别人的还不太一样。
    # append 是原地添加，返回值是 None
    # def pathSum(self, root: TreeNode, sum: int) -> int:
    #
    #     def dfs(root, sum_list):
    #         if not root:
    #             return 0
    #         sum_list = [num + root.val for num in sum_list] + [root.val]
    #         return sum_list.count(sum) + dfs(root.left, sum_list) + dfs(root.right, sum_list)
    #
    #     return dfs(root, [])

    # def pathSum(self, root: TreeNode, targetSum: int) -> int:
    #
    #     def dfs(root, cur):
    #         if not root:
    #             return 0
    #         cur = [num + root.val for num in cur] + [root.val]
    #         return cur.count(targetSum) + dfs(root.left, cur) + dfs(root.right, cur)
    #     return dfs(root, [])

    # 双重dfs，与第一个写的如初一辙
    # 不需要从根节点算起
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        def dfs(root, targetSum):
            if not root:
                return 0
            res = 0
            if root.val == targetSum:
                res += 1
            return res + dfs(root.left, targetSum-root.val) + dfs(root.right, targetSum-root.val)

        if not root:  # 因为后面用到了 root.left
            return 0
        # 注意下面的 dfs 写法
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
