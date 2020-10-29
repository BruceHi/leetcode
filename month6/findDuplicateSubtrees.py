# 寻找重复的子树
from typing import List
from collections import Counter
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
    #     res = []
    #     # count = Counter()
    #     count = defaultdict(int)
    #
    #     def serialize(node):
    #         if not node:
    #             return ''
    #         string = str(node.val) + ',' + serialize(node.left) + ',' + serialize(node.right)  # 两个逗号不能去掉
    #         count[string] += 1
    #         if count[string] == 2:  # 保证不管重复几次，只记录一次
    #             res.append(node)
    #         return string
    #
    #     serialize(root)
    #     return res

    # def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
    #     res = []
    #     record = set()
    #
    #     def serialize(node):
    #         if not node:
    #             return ''
    #         s = str(node.val) + ',' + serialize(node.left) + ',' + serialize(node.right)
    #         if s in record:
    #             res.append(node)
    #         else:
    #             record.add(s)
    #         return s
    #
    #     serialize(root)
    #     return res

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        dic = defaultdict(int)
        res = []

        def serialize(root):
            if not root:
                return ''
            s = str(root.val) + ',' + serialize(root.left) + ',' + serialize(root.right)
            dic[s] += 1
            if dic[s] == 2:
                res.append(root)
            return s
        serialize(root)
        return res

