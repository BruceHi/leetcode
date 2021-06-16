# 剑指offer 56-1. 数组中数字出现的次数
from typing import List
from collections import Counter


class Solution:
    # def singleNumbers(self, nums: List[int]) -> List[int]:
    #     counter = Counter(nums)
    #     res = []
    #     for i, val in counter.items():
    #         if val == 1:
    #             res.append(i)
    #     return res

    # 使用异或方法
    # def singleNumbers(self, nums: List[int]) -> List[int]:
    #     n = 0
    #     for num in nums:
    #         n ^= num
    #     m = n & -n  # 取末尾1
    #     x, y = 0, 0
    #     for num in nums:
    #         if num & m:
    #             x ^= num
    #         else:
    #             y ^= num
    #     return [x, y]

    def singleNumbers(self, nums: List[int]) -> List[int]:
        n = 0
        for num in nums:
            n ^= num
        m = n & -n

        x, y = 0, 0
        for num in nums:
            if m & num:
                x ^= num
            else:
                y ^= num
        return [x, y]


s = Solution()
nums = [4,1,4,6]
print(s.singleNumbers(nums))

nums = [1,2,10,4,1,4,3,3]
print(s.singleNumbers(nums))
