# 583. 把二叉搜索树转换为累加树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 反向中序遍历，操
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0

        def dfs(root):
            nonlocal total
            if not root:
                return
            dfs(root.right)
            total += root.val
            root.val = total
            dfs(root.left)

        dfs(root)
        return root

    # def convertBST(self, root: TreeNode) -> TreeNode:
    #     def dfs(root, total):
    #         if not root:
    #             return total
    #         root.val += dfs(root.right, total)
    #         return dfs(root.left, root.val)
    #
    #     dfs(root, 0)
    #     return root
