# 1005. k 次取反后最大化的数组和
from typing import List


class Solution:
    # def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
    #     nums.sort(key=lambda x: abs(x), reverse=True)
    #     for i, num in enumerate(nums):
    #         if num < 0:
    #             nums[i] = -num
    #             k -= 1
    #             if k == 0:
    #                 return sum(nums)
    #     if k & 1:
    #         return sum(nums) - 2 * nums[-1]
    #     return sum(nums)

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=abs, reverse=True)
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = -num
                k -= 1
                if k == 0:
                    return sum(nums)
        if k & 1:
            return sum(nums) - 2 * nums[-1]
        return sum(nums)

s = Solution()
nums = [4,2,3]
k = 1
print(s.largestSumAfterKNegations(nums, k))

nums = [3,-1,0,2]
k = 3
print(s.largestSumAfterKNegations(nums, k))

nums = [2,-3,-1,5,-4]
k = 2
print(s.largestSumAfterKNegations(nums, k))
