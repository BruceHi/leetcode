# **连续**子数组的最大和
from typing import List


class Solution:
    # def maxSubArray(self, nums):
    #     if not nums:
    #         return 0
    #     dp, max_val = float('-inf'), float('-inf')
    #     for num in nums:
    #         dp = max(num, dp+num)
    #         max_val = max(max_val, dp)
    #
    #     return max_val

    # dp[i] 表示 以 num[i] 为结尾的最长连续子数组长度。
    # def maxSubArray(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [0] * n
    #     dp[0] = nums[0]
    #     for i in range(1, n):
    #         if dp[i-1] > 0:
    #             dp[i] = dp[i-1] + nums[i]
    #         else:
    #             dp[i] = nums[i]
    #     return max(dp)

    # def maxSubArray(self, nums: List[int]) -> int:
    #     dp, max_val = float('-inf'), float('-inf')
    #     for num in nums:
    #         dp = max(num, dp + num)
    #         max_val = max(dp, max_val)
    #     return max_val

    # def maxSubArray(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [0] * n
    #     dp[0] = nums[0]
    #     for i in range(1, n):
    #         dp[i] = max(dp[i-1]+nums[i], nums[i])
    #     return max(dp)

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


s = Solution()
a = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(a))

# a = []
# print(s.maxSubArray(a))

a = [-2]
print(s.maxSubArray(a))
