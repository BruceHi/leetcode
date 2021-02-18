# 628. 三个数的最大乘积
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


s = Solution()
nums = [1,2,3]
print(s.maximumProduct(nums))

nums = [1,2,3,4]
print(s.maximumProduct(nums))

nums = [-1,-2,-3]
print(s.maximumProduct(nums))
