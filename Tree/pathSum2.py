# 437.路径总和3
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # # 双重dfs
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

    # 错误，由于执行 pathSun，res 就会重新归为 0
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
    #     if not root:
    #         return res
    #     search(root, sum)
    #     self.pathSum(root.left, sum)
    #     self.pathSum(root.right, sum)
    #     return res

    # 双重dfs，这个其实也用到了前缀和，但和别人的还不太一样。
    # append 是原地添加，返回值是 None
    def pathSum(self, root: TreeNode, sum: int) -> int:

        def dfs(root, sum_list):
            if not root:
                return 0
            sum_list = [num + root.val for num in sum_list] + [root.val]
            return sum_list.count(sum) + dfs(root.left, sum_list) + dfs(root.right, sum_list)

        return dfs(root, [])
