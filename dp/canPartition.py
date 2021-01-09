# 416. 分隔等和子集
# 0-1 背包问题
from typing import List


class Solution:
    # def canPartition(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     if n < 2:
    #         return False
    #     total = sum(nums)
    #     if total & 1:
    #         return False
    #     target = total >> 1
    #     if max(nums) > target:  # 最大值大于 target，则如何也不能分为两个子集
    #         return False
    #
    #     dp = [[False] * (target+1) for _ in range(n)]
    #     for i in range(n):
    #         dp[i][0] = True
    #
    #     # 0 号物品，背包容量刚好为nums[0]，肯定能填满。
    #     dp[0][nums[0]] = True
    #
    #     for i in range(1, n):
    #         num = nums[i]
    #         for j in range(1, target+1):
    #             if j > num:
    #                 dp[i][j] = dp[i-1][j] or dp[i-1][j-num]  # | 是位运算符，不能随便使用，否则结果还是 1 或 0
    #             else:
    #                 dp[i][j] = dp[i-1][j]
    #     return dp[n-1][target]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1
        if max(nums) > target:  # 最大值大于 target，则如何也不能分为两个子集
            return False

        dp = [[False] * (target+1) for _ in range(n)]  # 这个不能改
        for i in range(n):
            dp[i][0] = True

        # 0 号物品，背包容量刚好为nums[0]，肯定能填满。
        dp[0][nums[0]] = True

        for i in range(1, n):
            num = nums[i]
            for j in range(1, target+1):
                dp[i][j] = dp[i - 1][j]
                if j > num:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-num]  # | 是位运算符，不能随便使用，否则结果还是 1 或 0

        return dp[n-1][target]


s = Solution()
nums = [1, 5, 11, 5]
print(s.canPartition(nums))

nums = [1, 2, 3, 5]
print(s.canPartition(nums))

nums = [1]
print(s.canPartition(nums))


nums = [2, 2, 1, 1]
print(s.canPartition(nums))


nums = [2,2,3,5]
print(s.canPartition(nums))
