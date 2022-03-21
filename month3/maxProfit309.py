# 309. 最佳股票买卖时期含冷冻期
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n+2)]
        dp[0][1] = dp[1][1] = float('-inf')
        for i in range(2, n+2):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-2])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i-2])
        return dp[n+1][0]


s = Solution()
prices = [1,2,3,0,2]
print(s.maxProfit(prices))

prices = [1]
print(s.maxProfit(prices))
