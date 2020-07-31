# 魔术索引
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i == num:
                return i
        return -1


s = Solution()
nums = [0, 2, 3, 4, 5]
print(s.findMagicIndex(nums))

nums = [1, 1, 1]
print(s.findMagicIndex(nums))

nums = []
print(s.findMagicIndex(nums))
