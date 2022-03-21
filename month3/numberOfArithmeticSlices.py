# 413. 等差数列划分
from typing import List


class Solution:
    # 动态规划：dp[i] 是以a[i] 为终点的等差数列个数
    # 等差：A[i]-A[i-1] == A[i-1]-A[i-2]则dp[i] = dp[i-1] + 1
    # 否则：dp[i] = 0
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(1, n-1):
            if nums[i-1] + nums[i+1] == 2 * nums[i]:
                dp[i] = dp[i-1] + 1
        return sum(dp)



s = Solution()
nums = [1,2,3,4]
print(s.numberOfArithmeticSlices(nums))

nums = [1]
print(s.numberOfArithmeticSlices(nums))
