# 494. 目标和
from typing import List
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
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        res = 0

        def dfs(i, cur, remain_sum):
            nonlocal res
            if i == n:
                if cur == S:
                    res += 1
                return
            if cur + remain_sum < S or cur - remain_sum > S:
                return
            num = nums[i]
            dfs(i+1, cur+num, remain_sum-num)
            dfs(i+1, cur-num, remain_sum-num)

        dfs(0, 0, sum(nums))
        return res


s = Solution()
nums = [1, 1, 1, 1, 1]
S = 3
print(s.findTargetSumWays(nums, S))
