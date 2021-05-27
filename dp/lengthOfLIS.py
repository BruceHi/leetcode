# 300. 最长递增子序列的长度
from typing import List


class Solution:
    # def lengthOfLIS(self, nums) -> int:
    #     length = len(nums)
    #     if length < 1:
    #         return 0
    #     dp = [1] * length
    #     for i in range(1, length):
    #         for j in range(i):
    #             if nums[j] < nums[i]:  # 并非判断前面一个值小于，而是判断前面所有的值有没有小于的
    #                 dp[i] = max(dp[j]+1, dp[i])  # 让 dp[i] 始终为最大值
    #
    #     return max(dp)

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #     dp = [1] * n
    #
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1] * n
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #     return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


s = Solution()


c = [4,10,4,3,8,9]
print(s.lengthOfLIS(c))

c = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(c))

c = [1,3,6,7,9,4,10,5,6]
print(s.lengthOfLIS(c))

nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(nums))

nums = [0,1,0,3,2,3]
print(s.lengthOfLIS(nums))

nums = [7,7,7,7,7,7,7]
print(s.lengthOfLIS(nums))
