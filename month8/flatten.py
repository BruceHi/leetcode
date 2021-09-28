# 114. 二叉树展开为链表
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 1.递归方法
    # def flatten(self, root: TreeNode) -> None:
    #     def preorder(root):
    #         if not root:
    #             return []
    #         return [root] + preorder(root.left) + preorder(root.right)
    #
    #     nodes = preorder(root)
    #     for i, node in enumerate(nodes[:-1]):
    #         node.left, node.right = None, nodes[i+1]
    #

    # # 2.迭代与重组链表同时进行（这个看不懂）
    # def flatten(self, root: TreeNode) -> None:
    #     if not root:
    #         return
    #
    #     pre, stack = None, [root]
    #     while stack:
    #         cur = stack.pop()
    #         if pre:
    #             pre.left = None
    #             pre.right = cur
    #         left, right = cur.left, cur.right
    #         if right:
    #             stack.append(right)
    #         if left:
    #             stack.append(left)
    #         pre = cur

    # 3、不需要借助 stack，在原来的基础上构造链表, 空间复杂度是 O(1)
    # def flatten(self, root: TreeNode) -> None:
    #     pre = root
    #     while pre:
    #         cur = pre.left
    #         if cur:
    #             while cur.right:
    #                 cur = cur.right
    #             cur.right = pre.right
    #             pre.left, pre.right = None, pre.left
    #         pre = pre.right

    # 4、整体使用迭代
    # def flatten(self, root: TreeNode) -> None:
    #     if not root:
    #         return
    #     self.flatten(root.left)
    #     self.flatten(root.right)
    #
    #     cur = root.left
    #     if cur:
    #         while cur.right:  # cur 要找到左子树的最末一位
    #             cur = cur.right
    #         cur.right = root.right
    #         root.left, root.right = None, root.left

    # 写得不太好，没有注意这个是没有返回值的
    # def flatten(self, root: TreeNode) -> None:
    #     if not root:
    #         return
    #     a, b = self.flatten(root.left), self.flatten(root.right)
    #
    #     root.left = None
    #     cur = a
    #     if cur:
    #         while cur.right:
    #             cur = cur.right
    #         root.right = a
    #         cur.right = b
    #     else:
    #         root.right = b

    # 递归方法思路比较简单
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        cur = root.left
        if cur:
            while cur.right:
                cur = cur.right
            cur.right = root.right
            root.left, root.right = None, root.left
