# 673. 最长递增子序列的个数
from typing import List


class Solution:
    # def findNumberOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1] * n
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #     return dp

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        count = [1] * n
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        res = 0
        max_len = max(dp)
        for i in range(n):
            if max_len == dp[i]:
                res += count[i]
        return res






        return dp

s = Solution()
nums = [1,3,5,4,7]
print(s.findNumberOfLIS(nums))

nums = [2,2,2,2,2]
print(s.findNumberOfLIS(nums))
