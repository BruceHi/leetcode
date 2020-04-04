class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int):
        if not root:
            return
        if val == root.val:
            return root
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

    # # 迭代
    # def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    #     new_node = TreeNode(val)
    #     cur, tmp = root, root
    #     while cur:
    #         tmp = cur
    #         if val < cur.val:
    #             cur = cur.left
    #         else:
    #             cur = cur.right
    #     if val < tmp.val:  # tmp是最后一个结点
    #         tmp.left = new_node
    #     else:
    #         tmp.right = new_node
    #     return root

    # 递归
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def deleteNode(self, root: TreeNode, key: int):

        def successor(root):
            root = root.right
            while root.left:
                root = root.left
            return root.val

        def predecessor(root):
            root = root.left
            while root.right:
                root = root.right
            return root.val

        def delete(root, key):
            if not root:
                return None

            if key > root.val:
                root.right = self.deleteNode(root.right, key)
            elif key < root.val:
                root.left = self.deleteNode(root.left, key)
            else:
                if not (root.right or root.left):  # 叶节点
                    root = None
                elif root.right:
                    root.val = successor(root)  # 有右结点：只有右节点或左右结点都有
                    root.right = self.deleteNode(root.right, root.val)
                else:
                    root.val = predecessor(root)
                    root.left = self.deleteNode(root.left, root.val)
            return root

        return delete(root, key)
