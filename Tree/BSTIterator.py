# 二叉搜索树迭代器
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    # 递归方法
    def __init__(self, root: TreeNode):
        self.index = -1
        self.node_list = []
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.node_list.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.node_list[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.node_list)

    # 迭代方法
    def __init__(self, root: TreeNode):
        self.stack = []
        self.inorder_left(root)

    def inorder_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        top = self.stack.pop()
        if top.right:
            self.inorder_left(top.right)
        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
