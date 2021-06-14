# 最小栈，其实就是一个普通的栈
# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#
#     def pop(self) -> None:
#         if not self.stack:
#             return
#         self.stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return min(self.stack)
#
# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min_value = []
#
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         if not self.min_value or x <= self.min_value[-1]:
#             self.min_value.append(x)
#
#     def pop(self) -> None:
#         if not self.stack:
#             return
#         if self.stack.pop() == self.min_value[-1]:
#             self.min_value.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return self.min_value[-1]


# Your MinStack object will be instantiated and called as such:

# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min_stack = []
#
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         if not self.min_stack or x <= self.min_stack[-1]:
#             self.min_stack.append(x)
#
#     def pop(self) -> None:
#         if not self.stack:
#             return
#         if self.stack.pop() == self.min_stack[-1]:
#             self.min_stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return self.min_stack[-1]

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)

    def pop(self) -> None:
        if not self.stack:
            return
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
# print(minStack.getMin())  # --> 返回 -3.
print(minStack.min())  # --> 返回 -3.
minStack.pop()
print(minStack.top())  # --> 返回 0.
# print(minStack.getMin())  # --> 返回 -2.
print(minStack.min())  # --> 返回 -2.

# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
#
# minStack.pop()
# minStack.pop()
# minStack.pop()
# minStack.pop()

a = []
print(a.pop())
