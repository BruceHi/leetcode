# 703. 数据流中第 k 大元素

from typing import List
import heapq


# class KthLargest:
#
#     # def __init__(self, k: int, nums: List[int]):
#     #     self.pool = heapq.nlargest(k, nums)
#     #     heapq.heapify(self.pool)
#     #     print(type(self.pool))
#     #     # 返回值是由大到小排列，只要一逆序，就是一个小顶堆了。
#     #     # self.pool = heapq.nlargest(k, nums)[::-1]
#     #     # self.pool = sorted(nums, reverse=True)[:k][::-1]
#     #     self.k = k
#     #
#     # def add(self, val: int) -> int:
#     #     if len(self.pool) < self.k:
#     #         heapq.heappush(self.pool, val)
#     #     elif val > self.pool[0]:  # 不能是 if。
#     #         # heapq.heappushpop(self.pool, val)
#     #         heapq.heapreplace(self.pool, val)
#     #     return self.pool[0]
#
#     def __init__(self, k: int, nums: List[int]):
#         self.pool = heapq.nlargest(k, nums)
#         heapq.heapify(self.pool)
#         self.k = k
#
#     def add(self, val: int) -> int:
#         if len(self.pool) < self.k:
#             heapq.heappush(self.pool, val)
#         elif self.pool[0] < val:
#             heapq.heapreplace(self.pool, val)
#         return self.pool[0]

# class KthLargest:
#
#     def __init__(self, k: int, nums: List[int]):
#         self.pool = heapq.nlargest(k, nums)
#         heapq.heapify(self.pool)
#         self.k = k
#
#     def add(self, val: int) -> int:
#         if len(self.pool) < self.k:
#             heapq.heappush(self.pool, val)
#         elif self.pool[0] < val:
#             heapq.heapreplace(self.pool, val)
#         return self.pool[0]


# 超时
# class KthLargest:
#
#     def __init__(self, k: int, nums: List[int]):
#         self.nums = nums
#         self.k = k
#
#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         arr = self.nums[:self.k]
#         heapq.heapify(arr)
#         for num in self.nums[self.k:]:
#             if num > arr[0]:
#                 heapq.heappushpop(arr, num)
#         return arr[0]

# 始终维持一个大小为 k 的小顶堆
# class KthLargest:
#
#     def __init__(self, k: int, nums: List[int]):
#         self.pool = heapq.nlargest(k, nums)
#         heapq.heapify(self.pool)
#         self.k = k
#
#     def add(self, val: int) -> int:
#         if len(self.pool) < self.k:
#             heapq.heappush(self.pool, val)
#         elif val > self.pool[0]:
#             heapq.heappushpop(self.pool, val)
#         return self.pool[0]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.queue = nums
        heapq.heapify(self.queue)

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)
        while len(self.queue) > self.k:
            heapq.heappop(self.queue)
        return self.queue[0]

k = 3
nums = [4,5,8,2]
obj = KthLargest(k, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))

k = 1
nums = []
obj = KthLargest(k, nums)  # 初始化时，返回 pool = [], 即 nums 的长度还没 k 大。
print(obj.add(-3))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(0))
print(obj.add(4))



