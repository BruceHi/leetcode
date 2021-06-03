# 从前序/后序与中序遍历序列构造二叉树
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # # 中序和后序
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    #     if not inorder:
    #         return
    #     node = TreeNode(postorder[-1])
    #     i = inorder.index(node.val)
    #     node.left = self.buildTree(inorder[:i], postorder[:i])
    #     node.right = self.buildTree(inorder[i+1:], postorder[i:-1])
    #     return node

    # 前序和中序
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     if not preorder:
    #         return
    #     root = TreeNode(preorder[0])
    #     i = inorder.index(root.val)
    #     root.left = self.buildTree(preorder[1:i+1], inorder[:i])
    #     root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
    #     return root

    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    #     if not inorder:
    #         return
    #     root = TreeNode(postorder[-1])
    #     i = inorder.index(postorder[-1])
    #     root.left = self.buildTree(inorder[:i], postorder[:i])
    #     root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
    #     return root

    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    #     if not inorder:
    #         return
    #     val = postorder[-1]
    #     root = TreeNode(val)
    #     idx = inorder.index(val)
    #     root.left = self.buildTree(inorder[:idx], postorder[:idx])
    #     root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
    #     return root

    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     if not preorder:
    #         return
    #     val = preorder[0]
    #     root = TreeNode(val)
    #     i = inorder.index(val)
    #     root.left = self.buildTree(preorder[1:i+1], inorder[:i])
    #     root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
    #     return root

    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    #     if not inorder:
    #         return
    #     val = postorder[-1]
    #     root = TreeNode(val)
    #     i = inorder.index(val)
    #     root.left = self.buildTree(inorder[:i], postorder[:i])
    #     root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
    #     return root

    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     if not preorder:
    #         return
    #     val = preorder[0]
    #     root = TreeNode(val)
    #     i = inorder.index(val)
    #     root.left = self.buildTree(preorder[1:i+1], inorder[:i])
    #     root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
    #     return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        val = preorder[0]
        root = TreeNode(val)
        idx = inorder.index(val)
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root

