# 剑指 offer 36. 二叉搜索树与双向链表
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 只有一个节点的要与自身相连
    # def treeToDoublyList(self, root: 'Node') -> 'Node':
    #     def inorder(root):
    #         if not root:
    #             return []
    #         return inorder(root.left) + [root] + inorder(root.right)
    #
    #     nodes = inorder(root)
    #     if len(nodes) < 1:
    #         return root
    #     if len(nodes) == 1:
    #         nodes[0].left, nodes[0].right = nodes[0], nodes[0]
    #         return root
    #     nodes[0].left, nodes[0].right = nodes[-1], nodes[1]
    #     nodes[-1].left, nodes[-1].right = nodes[-2], nodes[0]
    #     for i in range(1, len(nodes)-1):
    #         nodes[i].left, nodes[i].right = nodes[i-1], nodes[i+1]
    #     return nodes[0]

    # def treeToDoublyList(self, root: 'Node') -> 'Node':
    #     def inorder(root):
    #         if not root:
    #             return []
    #         return inorder(root.left) + [root] + inorder(root.right)
    #
    #     if not root:
    #         return root
    #     if not root.left and not root.right:
    #         root.left, root.right = root, root
    #         return root
    #
    #     nodes = inorder(root)
    #     nodes[0].left, nodes[0].right = nodes[-1], nodes[1]
    #     nodes[-1].left, nodes[-1].right = nodes[-2], nodes[0]
    #     for i in range(1, len(nodes)-1):
    #         nodes[i].left, nodes[i].right = nodes[i-1], nodes[i+1]
    #     return nodes[0]

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)

        if not root:
            return root

        nodes = inorder(root)
        for i, node in enumerate(nodes):
            node.left, node.right = nodes[i-1], nodes[(i+1) % len(nodes)]
        return nodes[0]
