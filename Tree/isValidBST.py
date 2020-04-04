# 验证二叉搜索树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        inorder = inorder(root)
        return inorder == sorted(set(inorder))  # set只有判断有相同元素的出现，就False

class Solution:

    # 使用了中序遍历的迭代法，在迭代过程中进行判断，效率更高。
    def isValidBST(self, root: TreeNode) -> bool:
        stack, cur, inorder = [], root, float('-inf')
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            if top.val <= inorder:
                return False
            inorder = top.val
            cur = top.right
        return True




