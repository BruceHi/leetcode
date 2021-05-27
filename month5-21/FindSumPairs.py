from typing import List
from collections import Counter

# 超时
# class FindSumPairs:
#
#     def __init__(self, nums1: List[int], nums2: List[int]):
#         self.nums1 = nums1
#         self.nums2 = nums2
#
#     def add(self, index: int, val: int) -> None:
#         self.nums2[index] = self.nums2[index] + val
#
#     def count(self, tot: int) -> int:
#         res = 0
#         for num1 in self.nums1:
#             for num2 in self.nums2:
#                 if num1 + num2 == tot:
#                     res += 1
#         return res


# 还是超时
# class FindSumPairs:
#
#     def __init__(self, nums1: List[int], nums2: List[int]):
#         self.nums1 = nums1
#         self.nums2 = nums2
#
#     def add(self, index: int, val: int) -> None:
#         self.nums2[index] = self.nums2[index] + val
#
#     def count(self, tot: int) -> int:
#         res = 0
#         for num1 in sorted(self.nums1):
#             for num2 in sorted(self.nums2):
#                 if num1 + num2 == tot:
#                     res += 1
#                 elif num1 + num2 > tot:
#                     continue
#         return res


# 还是超时
# class FindSumPairs:
#
#     def __init__(self, nums1: List[int], nums2: List[int]):
#         self.nums1 = nums1
#         self.nums2 = nums2
#         self.counter = Counter(nums1)
#
#     def add(self, index: int, val: int) -> None:
#         self.nums2[index] = self.nums2[index] + val
#
#     def count(self, tot: int) -> int:
#         res = 0
#         for num in self.nums2:
#             if tot-num in self.counter:
#                 res += self.counter[tot-num]
#         return res

# 由于 nums1 的长度要远远小于 nums2 的长度，现遍历 nums1，统计 nums2的词频。
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.counter[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counter[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            if tot-num in self.counter:
                res += self.counter[tot-num]
        return res


nums1, nums2 = [1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]
s = FindSumPairs(nums1, nums2)
print(s.count(7))

s.add(3, 2)
print(s.nums2)

print(s.count(8))
print(s.count(4))

s.add(0, 1)
print(s.nums2)

s.add(1, 1)
print(s.nums2)

print(s.count(7))
