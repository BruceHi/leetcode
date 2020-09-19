# 连续子数组的最大乘积

# 不能照搬最大和的算法。因为负负得正。
# 需要定义取得的最小成绩，也要需要最小乘积。
# 要么是 num，即从 num 开始选取；要么是更新后的 cur_max， cur_min

from typing import List
class Solution:
    # def maxProduct(self, nums) -> int:
    #     if not nums:
    #         return 0
    #     res, cur_max, cur_min = nums[0], nums[0], nums[0]
    #     for i in range(1, len(nums)):
    #         num = nums[i]
    #         cur_max, cur_min = cur_max * num, cur_min*num
    #         cur_max, cur_min = max(cur_max, cur_min, num), min(cur_max, cur_min, num)
    #         res = max(cur_max, res)
    #     return res

    # 滚动数组
    # def maxProduct(self, nums) -> int:
    #     if not nums:
    #         return 0
    #     dp = [[0] * 2 for _ in range(2)]
    #     dp[0][0], dp[0][1], res = nums[0], nums[0], nums[0]
    #     for i in range(1, len(nums)):
    #         x, y, num = i % 2, (i-1) % 2, nums[i]
    #         dp[x][0] = max(dp[y][0] * num, dp[y][1] * num, num)
    #         dp[x][1] = min(dp[y][0] * num, dp[y][1] * num, num)
    #         res = max(res, dp[x][0])
    #     return res

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] * nums[i])
        return max(dp)


s = Solution()
a = [2,3,-2,4]
print(s.maxProduct(a))

a = [-2,0,-1]
print(s.maxProduct(a))

a = [-2,3,-4]
print(s.maxProduct(a))  # 24

