# 二叉搜索树迭代器
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class BSTIterator:
#
#     # 递归方法
#     def __init__(self, root: TreeNode):
#         self.index = -1
#         self.node_list = []
#         self._inorder(root)
#
#     def _inorder(self, root):
#         if not root:
#             return
#         self._inorder(root.left)
#         self.node_list.append(root.val)
#         self._inorder(root.right)
#
#     def next(self) -> int:
#         self.index += 1
#         return self.node_list[self.index]
#
#     def hasNext(self) -> bool:
#         return self.index + 1 < len(self.node_list)
#
#     # 迭代方法
#     def __init__(self, root: TreeNode):
#         self.stack = []
#         self.inorder_left(root)
#
#     def inorder_left(self, root):
#         while root:
#             self.stack.append(root)
#             root = root.left
#
#     def next(self) -> int:
#         top = self.stack.pop()
#         if top.right:
#             self.inorder_left(top.right)
#         return top.val
#
#     def hasNext(self) -> bool:
#         return len(self.stack) > 0

# class BSTIterator:
#
#     def __init__(self, root: TreeNode):
#
#         def inorder(root):
#             if not root:
#                 return []
#             return inorder(root.left) + [root.val] + inorder(root.right)
#         self.nums = deque(inorder(root))
#
#     def next(self) -> int:
#         """
#         @return the next smallest number
#         """
#         return self.nums.popleft()
#
#     def hasNext(self) -> bool:
#         """
#         @return whether we have a next smallest number
#         """
#         return self.nums != deque()
#         # return len(self.nums) > 0

# class BSTIterator:
#
#     def __init__(self, root: TreeNode):
#         def inorder(root):
#             if not root:
#                 return []
#             return inorder(root.left) + [root.val] + inorder(root.right)
#         self.nums = inorder(root)
#         self.i = 0
#
#     def next(self) -> int:
#         idx = self.i
#         self.i += 1
#         return self.nums[idx]
#
#     def hasNext(self) -> bool:
#         return self.i < len(self.nums)


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.inorder_left(root)

    def inorder_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        top = self.stack.pop()
        self.inorder_left(top.right)
        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


print(deque([]))
print(type(deque([])))

print(deque([]) == [])  # 与列表不是同一个数据类型，不相同
print(deque([]) == deque())  # 相同
print(deque([]) == deque([]))  # 相同

print(deque([]) == deque([1, 2]))  # 值不一样，不相同
