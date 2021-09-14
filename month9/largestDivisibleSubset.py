# 368. 最大整除子集
from typing import List


class Solution:
    #     # dp[i] = max(dp[j]+1, .....)
    # dp[i]表示以 nums[i] 为最大整数的「整除子集」的长度
    # val 表示最大的dp[i]时对应的整数
    # def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    #     nums.sort()
    #     n = len(nums)
    #     dp = [1] * n
    #     max_size, max_val = 1, 1
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[i] % nums[j] == 0:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #         if dp[i] > max_size:
    #             max_size, max_val = dp[i], nums[i]
    #
    #     if max_size == 1:
    #         return [nums[0]]
    #     res = []
    #     i = n - 1
    #     while i >= 0 and max_size > 0:
    #         if dp[i] == max_size and max_val % nums[i] == 0:
    #             res.append(nums[i])
    #             max_val = nums[i]
    #             max_size -= 1
    #         i -= 1
    #     return res

    # dp[i] 直接存放子集
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)


s = Solution()
nums = [1,2,3]
print(s.largestDivisibleSubset(nums))

nums = [1,2,4,8]
print(s.largestDivisibleSubset(nums))

nums = [3, 17]
print(s.largestDivisibleSubset(nums))

nums = [3, 4, 16, 8]
print(s.largestDivisibleSubset(nums))

nums = [4,8,10,240]
print(s.largestDivisibleSubset(nums))
