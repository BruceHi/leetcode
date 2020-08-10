class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 递归
    # def flatten(self, root: TreeNode) -> None:
    #
    #     def preorder(root):
    #         if not root:
    #             return []
    #         return [root] + preorder(root.left) + preorder(root.right)
    #
    #     order = preorder(root)
    #     for i in range(1, len(order)):
    #         pre, cur = order[i-1], order[i]
    #         pre.right = cur
    #         pre.left = None

    # # 迭代
    # def flatten(self, root: TreeNode) -> None:
    #     res, stack = [], []
    #     cur = root
    #     while cur or stack:
    #         while cur:
    #             res.append(cur)
    #             stack.append(cur)
    #             cur = cur.left
    #         top = stack.pop()
    #         cur = top.right
    #
    #     for i in range(1, len(res)):
    #         pre, cur = res[i-1], res[i]
    #         pre.right = cur
    #         pre.left = None

    #
    # # 迭代与重组链表同时进行
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

    # 不需要借助 stack，在原来的基础上构造链表, 空间复杂度是 O(1)
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                pre = nxt = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.left = None
                cur.right = nxt
            cur = cur.right

