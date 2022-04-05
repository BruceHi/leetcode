# 559. N 叉树的最大深度
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # def maxDepth(self, root: 'Node') -> int:
    #     if not root:
    #         return 0
    #     res = 1
    #     for child in root.children:
    #         res = max(res, 1+self.maxDepth(child))
    #     return res

    # def maxDepth(self, root: 'Node') -> int:
    #     if not root:
    #         return 0
    #     res = 1
    #     for node in root.children:
    #         res = max(res, self.maxDepth(node)+1)
    #     return res

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return depth + 1
