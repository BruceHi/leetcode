# 剑指 offer 59-2：队列的最大值
from collections import deque


# class MaxQueue:
#
#     def __init__(self):
#         self.queue = deque()
#
#     def max_value(self) -> int:
#         if not self.queue:
#             return -1
#         return max(self.queue)
#
#     def push_back(self, value: int) -> None:
#         self.queue.append(value)
#
#     def pop_front(self) -> int:
#         if not self.queue:
#             return -1
#         return self.queue.popleft()

class MaxQueue:

    # 辅助队列，从左到右，非递增数列
    def __init__(self):
        self.queue = deque()
        self.min_queue = deque()

    def max_value(self) -> int:
        if not self.queue:
            return -1
        return self.min_queue[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.min_queue and value > self.min_queue[-1]:
            self.min_queue.pop()
        self.min_queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        val = self.queue.popleft()
        if val == self.min_queue[0]:
            self.min_queue.popleft()
        return val


queue = MaxQueue()
queue.push_back(1)
queue.push_back(2)
print(queue.max_value())
print(queue.pop_front())
print(queue.max_value())

queue = MaxQueue()
print(queue.pop_front())
print(queue.max_value())
