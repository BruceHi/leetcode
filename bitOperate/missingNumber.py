# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
from functools import reduce
from operator import ixor
from typing import List

class Solution:
    # 数学方法
    # def missingNumber(self, nums) -> int:
    #     n = len(nums)
    #     return n * (n+1) // 2 - sum(nums)

    # 按位异或
    # def missingNumber(self, nums) -> int:
    #     res = len(nums)
    #     for i, num in enumerate(nums):
    #         res ^= i ^ num
    #     return res
    #
    #
    #     # n = len(nums)
    #     # res = 0
    #     # for i in range(n):
    #     #     res ^= i ^ nums[i]
    #     # return res ^ n
    #
    #     # return reduce(ixor, nums + list(range(len(nums)+1)))

    # 哈希表
    # def missingNumber(self, nums) -> int:
    #     nums = set(nums)
    #     for i in range(len(nums)+1):
    #         if i not in nums:
    #             return i

    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res


s = Solution()
nums = [3,0,1]
print(s.missingNumber(nums))

nums = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(nums))
