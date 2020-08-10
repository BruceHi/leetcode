# 给定一个二叉树，检查它是否是镜像对称的。
# 形状对称，数值对称

from collections import deque
from copy import deepcopy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 递归
    # def isSymmetric(self, root: TreeNode):
    #     def ismirr(t1, t2):
    #         if not (t1 or t2):  # 都为空
    #             return True
    #         if not (t1 and t2):  # 一个为空，一个不为空。本来还能判定两个都为空的情况，但是前面已经判定了，这里就不执行。
    #             return False
    #         return t1.val == t2.val and ismirr(t1.left, t2.right) and ismirr(t1.right, t2.left)
    #
    #     return ismirr(root, root)
    #

    # 迭代
    # def isSymmetric(self, root: TreeNode):
    #     queue = deque()
    #     queue.append(root)
    #     queue.append(root)
    #     while queue:
    #         t1, t2 = queue.popleft(), queue.popleft()
    #         if not t1 and not t2:  # 说明上一个节点是叶结点
    #             continue
    #         if not t1 or not t2:
    #             return False
    #         if t1.val != t2.val:
    #             return False
    #         queue.append(t1.left)
    #         queue.append(t2.right)
    #         queue.append(t1.right)
    #         queue.append(t2.left)
    #     return True

    # def isSymmetric(self, root: TreeNode):
    #
    #     def DFS(t1, t2):
    #         if not t1 and not t2:
    #             return True
    #         if not t1 or not t2:
    #             return False
    #         return t1.val == t2.val and DFS(t1.left, t2.right) and DFS(t1.right, t2.left)
    #
    #     return DFS(root, root)

    # def isSymmetric(self, root: TreeNode) -> bool:
    #
    #     def ismirr(r1, r2):
    #         if not r1 and not r2:
    #             return True
    #         if not r1 or not r2:
    #             return False
    #
    #         return r1.val == r2.val and ismirr(r1.left, r2.right) and ismirr(r1.right, r2.left)
    #
    #     return ismirr(root, root)

    def isSymmetric(self, root: TreeNode) -> bool:

        def symmetric(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left)

        return symmetric(root, root)

