# 面试题 17.16.按摩师
# 与打家劫舍 rob 一样
from typing import List


class Solution:
    # def massage(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #     dp = [0] * (n+1)
    #     dp[1] = nums[0]
    #     for i in range(2, n+1):
    #         dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
    #     return dp[n]

    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])   # 第一次 i-2 = -1，只是dp[-1]=0，所以不必担心越界
        return dp[n]


s = Solution()
nums = [1,2,3,1]
print(s.massage(nums))

nums = [2,7,9,3,1]
print(s.massage(nums))

nums = [2,1,4,5,3,1,1,3]
print(s.massage(nums))

nums = []
print(s.massage(nums))
