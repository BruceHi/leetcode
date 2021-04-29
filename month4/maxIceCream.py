# 5735. 雪糕的最大数量
from typing import List


class Solution:
    # 完全背包 错误
    # def maxIceCream(self, costs: List[int], coins: int) -> int:
    #     dp = [0] * (coins+1)
    #
    #     for cost in costs:
    #         for i in range(1, coins + 1):
    #             if i-cost >= 0:
    #                 dp[i] = max(dp[i], dp[i-cost]+1)
    #     return dp[coins]

    # 超时
    # def maxIceCream(self, costs: List[int], coins: int) -> int:
    #     if coins < min(costs):
    #         return 0
    #     m = len(costs)
    #     dp = [[0] * (coins+1) for _ in range(m+1)]
    #     for i in range(1, m+1):
    #         for j in range(1, coins+1):
    #             if costs[i-1] > j:
    #                 dp[i][j] = dp[i-1][j]
    #             else:
    #                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-costs[i-1]]+1)
    #     return dp[m][coins]

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        val = 0
        costs.sort()
        for i, cost in enumerate(costs):
            val += cost
            if val > coins:
                return i
        return len(costs)

s = Solution()
costs = [1,3,2,4,1]
coins = 7
print(s.maxIceCream(costs, coins))

costs = [10,6,8,7,7,8]
coins = 5
print(s.maxIceCream(costs, coins))

costs = [1,6,3,1,2,5]
coins = 20
print(s.maxIceCream(costs, coins))

