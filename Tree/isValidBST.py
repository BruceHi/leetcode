# 验证二叉搜索树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#
#     def isValidBST(self, root: TreeNode) -> bool:
#         def inorder(root):
#             if not root:
#                 return []
#             return inorder(root.left) + [root.val] + inorder(root.right)
#
#         inorder = inorder(root)
#         return inorder == sorted(set(inorder))  # set只有判断有相同元素的出现，就False

# class Solution:
#
#     # 使用了中序遍历的迭代法，在迭代过程中进行判断，效率更高。
#     def isValidBST(self, root: TreeNode) -> bool:
#         stack, cur, inorder = [], root, float('-inf')
#         while cur or stack:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left
#             top = stack.pop()
#             if top.val <= inorder:
#                 return False
#             inorder = top.val
#             cur = top.right
#         return True

class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    #
    #     def inorder(root):
    #         if not root:
    #             return []
    #         return inorder(root.left) + [root.val] + inorder(root.right)
    #
    #     res = inorder(root)
    #     return res == sorted(set(res))

    # # 迭代中判断，inorder 存储的相当于每个结点的左子树结点
    # def isValidBST(self, root: TreeNode) -> bool:
    #     stack, in_order = [], float('-inf')
    #     cur = root
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         top = stack.pop()
    #         if top.val <= in_order:
    #             return False
    #         in_order = top.val
    #         cur = top.right
    #     return True

    # 定义判断, 使用 DFS。
    # def isValidBST(self, root: TreeNode) -> bool:
    #
    #     def DFS(root, left, right):
    #         if not root:
    #             return True
    #
    #         return left < root.val < right and DFS(root.left, left, root.val) \
    #             and DFS(root.right, root.val, right)
    #
    #     return DFS(root, float('-inf'), float('inf'))

    # def isValidBST(self, root: TreeNode) -> bool:
    #
    #     def dfs(root, left, right):
    #         if not root:
    #             return True
    #         return left < root.val < right and dfs(root.left, left, root.val) \
    #                and dfs(root.right, root.val, right)
    #
    #     return dfs(root, float('-inf'), float('inf'))

    # def isValidBST(self, root: TreeNode) -> bool:
    #
    #     def inorder(root):
    #         if not root:
    #             return []
    #         return inorder(root.left) + [root.val] + inorder(root.right)
    #
    #     return inorder(root) == sorted(set(inorder(root)))

    # def isValidBST(self, root: TreeNode) -> bool:
    #     cur = root
    #     stack = []
    #     cmp = float('-inf')
    #
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         top = stack.pop()
    #         if top.val <= cmp:
    #             return False
    #         cmp = top.val
    #         cur = top.right
    #
    #     return True

    # def isValidBST(self, root: TreeNode) -> bool:
    #     def inorder(root):
    #         if not root:
    #             return []
    #         return inorder(root.left) + [root.val] + inorder(root.right)
    #
    #     return inorder(root) == sorted(set(inorder(root)))

    # def isValidBST(self, root: TreeNode) -> bool:
    #
    #     def dfs(root, left, right):
    #         if not root:
    #             return True
    #         return left < root.val < right and dfs(root.left, left, root.val) \
    #             and dfs(root.right, root.val, right)
    #
    #     return dfs(root, float('-inf'), float('inf'))

    # def isValidBST(self, root: TreeNode) -> bool:
    #
    #     def inorder(root):
    #         if not root:
    #             return []
    #         return inorder(root.left) + [root.val] + inorder(root.right)
    #     return inorder(root) == sorted(set(inorder(root)))

    # def isValidBST(self, root: TreeNode) -> bool:
    #     def dfs(root, left, right):
    #         if not root:
    #             return True
    #         return left < root.val < right and dfs(root.left, left, root.val) \
    #             and dfs(root.right, root.val, right)
    #
    #     return dfs(root, float('-inf'), float('inf'))

    def isValidBST(self, root: TreeNode) -> bool:

        def dfs(root, left, right):
            if not root:
                return True
            return left < root.val < right and dfs(root.left, left, root.val) and dfs(root.right, root.val, right)

        return dfs(root, float('-inf'), float('inf'))
