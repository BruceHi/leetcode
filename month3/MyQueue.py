# class MyQueue:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.stack = []
#         self.another = []
#
#     def push(self, x: int) -> None:
#         """
#         Push element x to the back of queue.
#         """
#         while self.stack:
#            self.another.append(self.stack.pop())
#         self.stack.append(x)
#         while self.another:
#             self.stack.append(self.another.pop())
#
#     def pop(self) -> int:
#         """
#         Removes the element from in front of queue and returns that element.
#         """
#         return self.stack.pop()
#
#
#     def peek(self) -> int:
#         """
#         Get the front element.
#         """
#         return self.stack[-1]
#
#
#     def empty(self) -> bool:
#         """
#         Returns whether the queue is empty.
#         """
#         return not self.stack

# 一个作为进栈，一个作为出栈
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_push = []
        self.stack_pop = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_push.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack_pop:
            return self.stack_pop.pop()
        while self.stack_push:
            self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack_pop:
            return self.stack_pop[-1]
        while self.stack_push:
            self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_push and not self.stack_pop


myQueue = MyQueue()
myQueue.push(1)  # queue is: [1]
myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek())  # return 1
print(myQueue.pop())  # return 1, queue is [2]
print(myQueue.empty())  # return false
