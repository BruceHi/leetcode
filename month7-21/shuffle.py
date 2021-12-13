# 打乱数组
import random
from copy import copy, deepcopy
from typing import List
from random import shuffle


# class Solution:
#
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.change = copy(nums)
#
#     def reset(self) -> List[int]:
#         """
#         Resets the array to its original configuration and return it.
#         """
#         return self.nums
#
#     def shuffle(self) -> List[int]:
#         """
#         Returns a random shuffling of the array.
#         """
#         shuffle(self.change)
#         return self.change

# Your Solution object will be instantiated and called as such:

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.another = deepcopy(nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        shuffle(self.another)
        return self.another


obj = Solution([1, 2, 3])
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
