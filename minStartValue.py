# 1413. 逐步求和得到正数的最小值
from typing import List


class Solution:
    # def minStartValue(self, nums: List[int]) -> int:
    #     prefix, min_val = 0, float('inf')
    #     for num in nums:
    #         prefix += num
    #         min_val = min(min_val, prefix)
    #     if min_val >= 0:
    #         return 1
    #     return 1 - min_val

    # def minStartValue(self, nums: List[int]) -> int:
    #     prefix, min_val = nums[0], nums[0]
    #     for num in nums[1:]:
    #         prefix += num
    #         min_val = min(min_val, prefix)
    #     if min_val >= 0:
    #         return 1
    #     return -min_val + 1

    def minStartValue(self, nums: List[int]) -> int:
        prefix, min_val = 0, float('inf')
        for num in nums:
            prefix += num
            min_val = min(min_val, prefix)
        if min_val > 0:
            return 1
        return 1 - min_val


s = Solution()
nums = [-3,2,-3,4,2]
print(s.minStartValue(nums))

nums = [1,2]
print(s.minStartValue(nums))

nums = [1,-2,-3]
print(s.minStartValue(nums))
