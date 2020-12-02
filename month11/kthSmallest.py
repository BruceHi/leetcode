# 230.二叉搜索树第 k 小的元素
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归，时间复杂度是 O(n)
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     def inorder(root):
    #         if not root:
    #             return []
    #         return inorder(root.left) + [root.val] + inorder(root.right)
    #
    #     return inorder(root)[k-1]

    # 迭代，时间复杂度是 O(H + k)，H 为二叉搜索树的高度
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            k -= 1
            if not k:
                return top.val
            cur = top.right
