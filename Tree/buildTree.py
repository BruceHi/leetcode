# 从前序与中序遍历序列构造二叉树（不会啊，哭卿卿）
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = None
        for num in preorder:
            root = TreeNode(num)
