# 二叉树 & 二叉搜索树的最近公共祖先
# Definition for a binary tree node.
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # # 二叉树
    # def lowestCommonAncestor(self, root, p, q):
    #     if not root:
    #         return
    #     if root == p or root == q:
    #         return root
    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)
    #     if left and right:
    #         return root
    #     if not left:
    #         return right
    #     if not right:
    #         return left

    # # 二叉搜索树 递归
    # def lowestCommonAncestor(self, root, p, q):
    #     if p.val < root.val > q.val:
    #         return self.lowestCommonAncestor(root.left, p, q)
    #     if p.val > root.val < q.val:
    #         return self.lowestCommonAncestor(root.right, p, q)
    #     return root

    # 二叉搜索树 迭代
    # def lowestCommonAncestor(self, root, p, q):
    #     while root:
    #         if p.val < root.val > q.val:
    #             root = root.left
    #         elif p.val > root.val < q.val:
    #             root = root.right
    #         else:  # 对于二叉搜索树而言，不会先出现一个大于结点一个小于结点的，肯定先出现的是等于某个结点。
    #             return root

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if not root:
    #         return
    #     if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
    #         return root
    #     if p.val > root.val and q.val > root.val:
    #         return self.lowestCommonAncestor(root.right, p, q)
    #     return self.lowestCommonAncestor(root.left, p, q)

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if p.val < root.val > q.val:
    #         return self.lowestCommonAncestor(root.left, p, q)
    #     if p.val > root.val < q.val:
    #         return self.lowestCommonAncestor(root.right, p, q)
    #     return root

    # 二叉树
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if not root:  # 退出条件
    #         return
    #     if root.val == p.val or root.val == q.val:
    #         return root
    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)
    #     if left and right:
    #         return root
    #     if left:
    #         return left
    #     if root:
    #         return right

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if not root:
    #         return
    #     if root.val == p.val or root.val == q.val:
    #         return root
    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)
    #     if left and right:
    #         return root
    #     if left:
    #         return left
    #     if right:
    #         return right

    # 二叉搜索树
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if p is root or q is root:
    #         return root
    #     v = root.val
    #     if p.val < v < q.val or p.val > v > q.val:
    #         return root
    #     if p.val < v and q.val < v:
    #         return self.lowestCommonAncestor(root.left, p, q)
    #     return self.lowestCommonAncestor(root.right, p, q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


    # 二叉树
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if not root:
    #         return
    #     if p is root or q is root:
    #         return root
    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)
    #     if left and right:
    #         return root
    #     return left or right
