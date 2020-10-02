# 二叉树的序列化和反序列化
# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # def serialize(self, root):
    #     if not root:
    #         return '[]'
    #     res, queue = [], deque([root])
    #
    #     while queue:
    #         for _ in range(len(queue)):
    #             tmp = queue.popleft()
    #             res.append(tmp.val)
    #             if tmp.left:
    #                 queue.append(tmp.left)
    #             else:
    #                 queue.append(TreeNode(None))
    #             if tmp.right:
    #                 queue.append(tmp.right)
    #             else:
    #                 queue.append(TreeNode(None))
    #     return str(res)

    # def serialize(self, root):
    #     if not root:
    #         return 'None,'
    #     res, queue = '', deque([root])
    #
    #     while queue:
    #         for _ in range(len(queue)):
    #             tmp = queue.popleft()
    #             res += tmp.val
    #             if tmp.left:
    #                 queue.append(tmp.left)
    #             else:
    #                 queue.append(TreeNode('None,'))
    #             if tmp.right:
    #                 queue.append(tmp.right)
    #             else:
    #                 queue.append(TreeNode('None,'))
    #     return res
    #
    # def deserialize(self, data):
    #     data = data.split(',')  # 两句不能写一块
    #     data.pop()
    #     if not data:
    #         return
    #     for char in data:
    #         T

    # 使用 DFS
    # def serialize(self, root):
    #
    #     # 前序遍历
    #     def dfs(root):
    #         if not root:
    #             return 'None,'  # 不会有空字符串产生
    #         return str(root.val) + ',' + dfs(root.left) + dfs(root.right)
    #     return dfs(root)
    #
    #
    #
    # def deserialize(self, data):
    #     def dfs(data):
    #         val = data.pop(0)
    #         if val == 'None':
    #             return
    #         node = TreeNode(val)
    #         node.left = dfs(data)
    #         node.right = dfs(data)
    #         return node
    #
    #     data = data.split(',')
    #     data.pop()
    #     return dfs(data)

    def serialize(self, root):
        def inorder(root):
            if not root:
                return 'None,'
            return str(root.val) + ',' + inorder(root.left) + inorder(root.right)
        return inorder(root)

    def deserialize(self, data):

        def dfs(data):
            if not data:
                return
            val = data.popleft()
            if val == 'None':
                return
            root = TreeNode(val)
            root.left = dfs(data)
            root.right = dfs(data)
            return root

        data = data.split(',')
        data.pop()
        return dfs(deque(data))



