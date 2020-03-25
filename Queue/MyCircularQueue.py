from typing import Optional
from itertools import chain

# class MyCircularQueue:
#
#     def __init__(self, k: int):
#         """
#         Initialize your data structure here. Set the size of the queue to be k.
#         """
#         self.queue = []
#         self.head = 0
#         # self.count = 0  # 队列（当前）长度，要它的时候queue不是空的列表。
#         self.tail = 0  # 需要tail,可以直接定义None的列表。需要计算长度，可以避免浪费。
#         self.capacity = k  # 队列容量（数组长度）
#
#     # 判断队空还是队满，只需比较容量和队列长度即可，根本不需要空一格，用尾指针与头指针的关系。不要记公式。
#     def enQueue(self, value: int) -> bool:
#         """
#         Insert an element into the circular queue. Return true if the operation is successful.
#         """
#         if len(self.queue) == self.capacity:
#             return False
#         self.queue.append(value)
#         # self.tail = (self.tail + 1) % self.capacity
#         return True
#
#     def deQueue(self) -> bool:
#         """
#         Delete an element from the circular queue. Return true if the operation is successful.
#         """
#         if len(self.queue) == 0:  # 空队列
#             return False
#         self.queue.pop(0)
#         # self.head += 1
#         return True
#
#     def Front(self) -> int:
#         """
#         Get the front item from the queue.
#         """
#         # if self.head == self.tail:  # 空队列（使用它时，必须要移动head,否则head始终为0）
#         if len(self.queue) == 0:
#             return -1
#         return self.queue[0]
#
#     def Rear(self) -> int:
#         """
#         Get the last item from the queue.
#         """
#         if len(self.queue) == 0:
#             return -1
#         return self.queue[-1]
#
#     def isEmpty(self) -> bool:
#         """
#         Checks whether the circular queue is empty or not.
#         """
#         return len(self.queue) == 0
#
#     def isFull(self) -> bool:
#         """
#         Checks whether the circular queue is full or not.
#         """
#         return len(self.queue) == self.capacity
#
#     def __repr__(self) -> str:
#         # if self.tail >= self.head:
#         return str(self.queue)
#         # else:
#         #     return


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.count = 0  # 队列（当前）长度，要它的时候queue不是空的列表。
        self.capacity = k  # 队列容量（数组长度）

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        self.queue.append(value)
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:  # 空队列
            return False
        self.queue.pop(0)  # 从头删除时间复杂度变成了O(n)
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[0]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity

    def __repr__(self) -> str:
        return str(self.queue)


if __name__ == "__main__":
    q = MyCircularQueue(5)
    for i in range(5):
        q.enQueue(i)
    q.deQueue()
    q.deQueue()
    q.enQueue(5)
    print(q)
