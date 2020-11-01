# 根据前序和后序遍历构造二叉树
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    #     if not pre:
    #         return
    #     root = TreeNode(pre[0])
    #     if len(pre) == 1:
    #         return root
    #     i = pre.index(post[-2])
    #     root.left = self.constructFromPrePost(pre[1:i], post[:i-1])
    #     root.right = self.constructFromPrePost(pre[i:], post[i-1:-1])
    #     return root

    # def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    #     if not pre:
    #         return
    #     root = TreeNode(pre[0])
    #     if len(pre) == 1:
    #         return root
    #     i = pre.index(post[-2])
    #     root.left = self.constructFromPrePost(pre[1:i], post[:i-1])
    #     root.right = self.constructFromPrePost(pre[i:], post[i-1:-1])
    #     return root

    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        i = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1:i+2], post[:i+1])
        root.right = self.constructFromPrePost(pre[i+2:], post[i+1:])
        return root
