# 恢复二叉搜索树


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 递归 只会显式中序遍历
    def recoverTree(self, root: TreeNode) -> None:

        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)

        node_list = inorder(root)
        sort_list = sorted(node_list, key=lambda node: node.val)
        p, q = [node for i, node in enumerate(node_list) if node.val != sort_list[i].val]
        # node1, node2 = [node1 for node1, node2 in zip(node_list, sort_list) if node1.val != node2.val]
        p.val, q.val = q.val, p.val

    # 错误的代码。
    # def recoverTree(self, root: TreeNode) -> None:
    #     cur = root
    #     stack = []
    #     record = float('-inf')
    #     res = []
    #
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         top = stack.pop()
    #         if not len(res):
    #             res.append(top)
    #         if top.val < record:
    #             res.append(top)
    #             if len(res) == 3:
    #                 break
    #         record = top.val
    #         cur = top.right
    #
    #     if len(res) == 2:
    #         p, q = res
    #     else:
    #         _, p, q = res
    #     p.val, q.val = q.val, p.val


