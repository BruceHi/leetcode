# 225. 用队列模拟栈
# # 1. 偷懒解法
# class MyStack:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.stack = []
#
#
#     def push(self, x: int) -> None:
#         """
#         Push element x onto stack.
#         """
#         self.stack.append(x)
#
#
#     def pop(self) -> int:
#         """
#         Removes the element on top of the stack and returns that element.
#         """
#         return self.stack.pop()
#
#     def top(self) -> int:
#         """
#         Get the top element.
#         """
#         return self.stack[-1]
#
#
#     def empty(self) -> bool:
#         """
#         Returns whether the stack is empty.
#         """
#         return not self.stack

from collections import deque

# 2.用队列模拟栈
# 队列是先进先出的，所以对于队列，不应该使用 self.pop 方法的。
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue