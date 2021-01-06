# 剑指 offer 59-2：队列的最大值
from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue = deque()

    def max_value(self) -> int:
        if not self.queue:
            return -1
        return max(self.queue)

    def push_back(self, value: int) -> None:
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        return self.queue.popleft()


queue = MaxQueue()
queue.push_back(1)
queue.push_back(2)
print(queue.max_value())
print(queue.pop_front())
print(queue.max_value())

queue = MaxQueue()
print(queue.pop_front())
print(queue.max_value())
