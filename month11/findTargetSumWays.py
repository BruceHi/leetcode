# 494. 目标和
from typing import List
# 有返回值的可以用 lru_cache，没有的不可以用缓存
from functools import lru_cache


class Solution:
    # 超时
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     if sum(nums) < S or -sum(nums) > S:
    #         return 0
    #
    #     n = len(nums)
    #     res = 0
    #
    #     def dfs(i, cur):
    #         nonlocal res
    #         if i == n - 1:
    #             if cur + nums[i] == S:
    #                 res += 1
    #             if cur - nums[i] == S:
    #                 res += 1
    #             return
    #         if cur + sum(nums[i:]) < S or cur - sum(nums[i:]) > S:
    #             return
    #         dfs(i+1, cur+nums[i])
    #         dfs(i+1, cur-nums[i])
    #
    #     dfs(0, 0)
    #     return res

    # 同样超时
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     n = len(nums)
    #     res = 0
    #
    #     def dfs(i, cur):
    #         nonlocal res
    #         if i == n:
    #             if cur == S:
    #                 res += 1
    #             return
    #         if cur + sum(nums[i:]) < S or cur - sum(nums[i:]) > S:
    #             return
    #         dfs(i+1, cur+nums[i])
    #         dfs(i+1, cur-nums[i])
    #
    #     dfs(0, 0)
    #     return res

    # 超时，即使做了剪枝也超时了。时间复杂度是 O(2^n)
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     n = len(nums)
    #     res = 0
    #
    #     def dfs(i, cur, remain_sum):
    #         nonlocal res
    #         if i == n:
    #             if cur == S:
    #                 res += 1
    #             return
    #         if cur + remain_sum < S or cur - remain_sum > S:
    #             return
    #         num = nums[i]
    #         dfs(i+1, cur+num, remain_sum-num)
    #         dfs(i+1, cur-num, remain_sum-num)
    #
    #     dfs(0, 0, sum(nums))
    #     return res

    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     n = len(nums)
    #     res = 0
    #
    #     def dfs(i, cur):
    #         nonlocal res
    #         if i == n:
    #             if cur == S:
    #                 res += 1
    #             return
    #         num = nums[i]
    #         dfs(i+1, cur+num)
    #         dfs(i+1, cur-num)
    #
    #     dfs(0, 0)
    #     return res

    # 失败
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     n = len(nums)
    #     dp = [[0] * (S+1) for _ in range(n+1)]
    #     dp[0][0] = 1
    #     for i in range(1, n+1):
    #         for j in range(1, S+1):
    #             dp[i][j] = dp[i-1][j]
    #             if j >= nums[i-1]:
    #                 dp[i][j] += dp[i][j-nums[i-1]]
    #     return dp[n][S]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i, cur):
            if i == n:
                if cur == target:
                    return 1
                return 0
            return dfs(i+1, cur+nums[i]) + dfs(i+1, cur-nums[i])

        return dfs(0, 0)


s = Solution()
nums = [1, 1, 1, 1, 1]
target = 3
print(s.findTargetSumWays(nums, target))
