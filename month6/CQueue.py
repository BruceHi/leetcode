# 剑指 Offer 09. 用两个栈实现队列
# class CQueue:
#
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#
#     def appendTail(self, value: int) -> None:
#         self.stack1.append(value)
#
#     # def deleteHead(self) -> int:
#     #     if not self.stack1:
#     #         return -1
#     #     while self.stack1:
#     #         self.stack2.append(self.stack1.pop())
#     #     val = self.stack2.pop()
#     #     while self.stack2:
#     #         self.stack1.append(self.stack2.pop())
#     #     return val
#
#     def deleteHead(self) -> int:  # 把要删除的元素按逆序放入栈中，若不为空直接删除即可。
#         if self.stack2:
#             return self.stack2.pop()
#         if not self.stack1:
#             return -1
#         while self.stack1:
#             self.stack2.append(self.stack1.pop())
#         return self.stack2.pop()

class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


obj = CQueue()
obj.appendTail(3)
print(obj.deleteHead())
print(obj.deleteHead())


print(obj.deleteHead())
obj.appendTail(5)
obj.appendTail(2)
print(obj.deleteHead())
print(obj.deleteHead())
