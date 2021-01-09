# 746. 使用最小花费爬楼梯
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        dp = [0] * (n+1)

        for i in range(1, n+1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i-1]
        return min(dp[n], dp[n-1])


s = Solution()
cost = [10, 15, 20]
print(s.minCostClimbingStairs(cost))

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(s.minCostClimbingStairs(cost))

cost = []
print(s.minCostClimbingStairs(cost))

cost = [1]
print(s.minCostClimbingStairs(cost))

cost = [1, 2]
print(s.minCostClimbingStairs(cost))