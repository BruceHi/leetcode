# 设计循环队列

# # 这种方法没有达到空间的循环利用，不太好。
# class MyCircularQueue:
#
#     def __init__(self, k: int):
#         """
#         Initialize your data structure here. Set the size of the queue to be k.
#         """
#         self.queue = []  # 使用可扩展的列表，才不会出现溢出问题，妙啊。
#         self.capacity = k  # 队列容量（数组长度）
#
#     def enQueue(self, value: int) -> bool:
#         """
#         Insert an element into the circular queue. Return true if the operation is successful.
#         """
#         if len(self.queue) == self.capacity:  # 判断队空还是队满，只需比较容量和队列长度即可
#             return False
#         self.queue.append(value)
#         return True
#
#     # 时间复杂度为 O(n)，不太好。
#     def deQueue(self) -> bool:
#         """
#         Delete an element from the circular queue. Return true if the operation is successful.
#         """
#         if not self.queue:
#             return False
#         self.queue.pop(0)
#         return True
#
#     def Front(self) -> int:
#         """
#         Get the front item from the queue.
#         """
#         if not self.queue:
#             return -1
#         return self.queue[0]
#
#     def Rear(self) -> int:
#         """
#         Get the last item from the queue.
#         """
#         if not self.queue:
#             return -1
#         return self.queue[-1]
#
#     def isEmpty(self) -> bool:
#         """
#         Checks whether the circular queue is empty or not.
#         """
#         return not self.queue
#
#     def isFull(self) -> bool:
#         """
#         Checks whether the circular queue is full or not.
#         """
#         return len(self.queue) == self.capacity
#
#     def __repr__(self) -> str:
#         return str(self.queue)

# 真正的循环队列，时间复杂度都是 O(1)。
# class MyCircularQueue:
#
#     def __init__(self, k: int):
#         """
#         Initialize your data structure here. Set the size of the queue to be k.
#         """
#         self.queue = [0] * (k + 1)  # 要多留一个长度
#         self.head = 0
#         self.tail = 0
#         self.capacity = k + 1  # 后面要多次用到，所以保留了。
#
#     def enQueue(self, value: int) -> bool:
#         """
#         Insert an element into the circular queue. Return true if the operation is successful.
#         """
#         if self.isFull():
#             return False
#         self.queue[self.tail] = value
#         self.tail = (self.tail + 1) % self.capacity  # 往后移一位，再求余
#         return True
#
#     def deQueue(self) -> bool:
#         """
#         Delete an element from the circular queue. Return true if the operation is successful.
#         """
#         if self.isEmpty():
#             return False
#
#         # 不需要改变值，直接移动指针即可。
#         self.head = (self.head + 1) % self.capacity
#         return True
#
#     def Front(self) -> int:
#         """
#         Get the front item from the queue.
#         """
#         if self.isEmpty():
#             return -1
#         return self.queue[self.head]
#
#     def Rear(self) -> int:
#         """
#         Get the last item from the queue.
#         """
#         if self.isEmpty():
#             return -1
#         # + capacity 是为了保证 tail=0 时，可以正常得出结果。
#         return self.queue[(self.tail - 1 + self.capacity) % self.capacity]
#
#     def isEmpty(self) -> bool:
#         """
#         Checks whether the circular queue is empty or not.
#         """
#         return self.head == self.tail
#
#     def isFull(self) -> bool:
#         """
#         Checks whether the circular queue is full or not.
#         """
#         return (self.tail + 1) % self.capacity == self.head

# class MyCircularQueue:
#
#     def __init__(self, k: int):
#         self.queue = [0] * (k + 1)
#         self.head = 0
#         self.tail = 0
#         self.capacity = k + 1
#
#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         self.queue[self.tail] = value
#         self.tail = (self.tail + 1) % self.capacity
#         return True
#
#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.head = (self.head + 1) % self.capacity
#         return True
#
#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.head]
#
#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.tail-1]
#
#     def isEmpty(self) -> bool:
#         return self.tail == self.head
#
#     def isFull(self) -> bool:
#         return (self.tail + 1) % self.capacity == self.head

# class MyCircularQueue:
#
#     def __init__(self, k: int):
#         self.nums = (k + 1) * [0]
#         self.capacity = k + 1
#         self.head = 0
#         self.tail = 0
#
#
#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         self.nums[self.tail] = value
#         self.tail = (self.tail + 1) % self.capacity
#         return True
#
#
#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.head = (self.head + 1) % self.capacity
#         return True
#
#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.nums[self.head]
#
#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.nums[self.tail - 1]
#
#     def isEmpty(self) -> bool:
#         return self.head == self.tail
#
#     def isFull(self) -> bool:
#         return (self.tail + 1) % self.capacity == self.head

# 右进左出
# class MyCircularQueue:
#
#     def __init__(self, k: int):
#         self.nums = [0] * (k+1)
#         self.capacity = k + 1
#         self.head = 0
#         self.tail = 0
#
#     # 右边是尾部
#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         self.nums[self.tail] = value
#         self.tail = (self.tail + 1) % self.capacity
#         return True
#
#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.head = (self.head + 1) % self.capacity
#         return True
#
#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.nums[self.head]
#
#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.nums[self.tail-1]
#
#     def isEmpty(self) -> bool:
#         return self.head == self.tail
#
#     def isFull(self) -> bool:
#         return (self.tail + 1) % self.capacity == self.head

# class MyCircularQueue:
#
#     def __init__(self, k: int):
#         self.nums = [0] * (k+1)
#         self.capacity = k + 1
#         self.head = 0
#         self.tail = 0
#
#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         self.nums[self.tail % self.capacity] = value
#         self.tail = (self.tail + 1) % self.capacity
#         return True
#
#
#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.head = (self.head + 1) % self.capacity
#         return True
#
#
#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.nums[self.head]
#
#
#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.nums[self.tail-1]
#
#
#     def isEmpty(self) -> bool:
#         return self.head == self.tail
#
#
#     def isFull(self) -> bool:
#         return (self.tail + 1) % self.capacity == self.head


# 入队的时候是 tail + 1，即队尾加
class MyCircularQueue:

    def __init__(self, k: int):
        self.nums = [0] * (k + 1)
        self.capacity = k + 1
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.nums[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.nums[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.nums[self.tail-1]

    def isEmpty(self) -> bool:
        return self.tail == self.head

    def isFull(self) -> bool:
        return (self.tail + 1) % self.capacity == self.head


if __name__ == "__main__":
    q = MyCircularQueue(5)
    for i in range(5):
        q.enQueue(i)
    q.deQueue()
    q.deQueue()
    q.enQueue(5)
    print(q.nums)

    circularQueue = MyCircularQueue(3)
    print(circularQueue.enQueue(1))
    print(circularQueue.enQueue(2))
    print(circularQueue.enQueue(3))
    print(circularQueue.enQueue(4))
    print(circularQueue.Rear())
    print(circularQueue.isFull())
    print(circularQueue.deQueue())
    print(circularQueue.enQueue(4))
    print(circularQueue.Rear())
