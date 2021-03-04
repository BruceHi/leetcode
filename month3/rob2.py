# 213.打家劫舍 2
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            n = len(nums)
            dp = [0] * (n+1)
            for i in range(1, n+1):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            return dp[n]

        return max(my_rob(nums[1:]), my_rob(nums[:-1])) if len(nums) != 1 else nums[0]


s = Solution()
nums = [2,3,2]
print(s.rob(nums))

nums = [1,2,3,1]
print(s.rob(nums))

nums = [0]
print(s.rob(nums))

nums = [1]
print(s.rob(nums))

nums = [1, 2]
print(s.rob(nums))

nums = [1,2,1,1]
print(s.rob(nums))
