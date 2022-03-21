# 590.N 叉树的后序遍历
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # def postorder(self, root: 'Node') -> List[int]:
    #     if not root:
    #         return []
    #     res = []
    #     for child in root.children:
    #         res += self.postorder(child)
    #     res.append(root.val)
    #     return res

    # def postorder(self, root: 'Node') -> List[int]:
    #     if not root:
    #         return []
    #     stack, res = [root], []
    #     while stack:
    #         cur = stack.pop()
    #         res.append(cur.val)
    #         stack.extend(cur.children)
    #     return res[::-1]

    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        for node in root.children:
            res.extend(self.postorder(node))
        res.append(root.val)
        return res
