# 打家劫舍
from typing import List


class Solution:
    # def rob(self, nums) -> int:
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #     steal, not_steal = 0, 0  # dp[i-1]
    #     for num in nums:
    #         steal_tmp = steal
    #         steal = not_steal + num
    #         not_steal = max(not_steal, steal_tmp)
    #     return max(steal, not_steal)

    # def rob(self, nums) -> int:
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #
    #     dp_0, dp_1 = [0] * (n+1), [0] * (n+1)  # 0:不偷， 1：偷
    #     for i in range(1, n+1):
    #         dp_1[i] = dp_0[i-1] + nums[i-1]
    #         dp_0[i] = max(dp_0[i-1], dp_1[i-1])
    #     return max(dp_0[n], dp_1[n])

    # def rob(self, nums) -> int:
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #
    #     dp = [0] * (n+2)
    #     for i in range(2, n+2):
    #         dp[i] = max(dp[i-2]+nums[i-2], dp[i-1])
    #     return dp[n+1]

    # def rob(self, nums) -> int:
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #
    #     dp, old_dp = 0, 0
    #     for num in nums:
    #         tmp = dp
    #         dp = max(old_dp+num, dp)
    #         old_dp = tmp
    #     return dp

    def rob(self, nums: List[int]) -> int:
        dp, dp_old = 0, 0
        for num in nums:
            tmp = dp
            dp = max(dp_old+num, dp)
            dp_old = tmp
        return dp



s = Solution()
a = [1,2,3,1]
print(s.rob(a))

a = [2,7,9,3,1]
print(s.rob(a))
