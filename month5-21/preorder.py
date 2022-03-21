from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # def preorder(self, root: 'Node') -> List[int]:
    #     res = []
    #
    #     def dfs(root):
    #         if not root:
    #             return
    #         res.append(root.val)
    #         for child in root.children:
    #             if child:
    #                 dfs(child)
    #     dfs(root)
    #     return res

    # def preorder(self, root: 'Node') -> List[int]:
    #     if not root:
    #         return []
    #     res = [root.val]
    #     for child in root.children:
    #         res += self.preorder(child)
    #     return res

    # def preorder(self, root: 'Node') -> List[int]:
    #     if not root:
    #         return []
    #     stack, res = [root], []
    #     while stack:
    #         cur = stack.pop()
    #         res.append(cur.val)
    #         for child in reversed(cur.children):
    #             stack.append(child)
    #     return res

    # def preorder(self, root: 'Node') -> List[int]:
    #     if not root:
    #         return []
    #     stack, res = [root], []
    #     while stack:
    #         cur = stack.pop()
    #         res.append(cur.val)
    #         stack.extend(cur.children[::-1])
    #     return res

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = [root.val]
        for node in root.children:
            res.extend(self.preorder(node))
        return res
