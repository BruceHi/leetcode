# 122.买卖股票的最佳时机2
# 允许交易多次
from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     res = 0
    #     for i in range(1, len(prices)):
    #         if prices[i] > prices[i-1]:
    #             res += prices[i] - prices[i-1]
    #     return res

    # 动态规划
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     dp = [[0, 0] for _ in range(n+1)]
    #
    #     dp[0][1] = float('-inf')
    #     for i in range(1, n+1):
    #         dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
    #         dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i-1])
    #     return dp[n][0]

    # 状态压缩
    # def maxProfit(self, prices: List[int]) -> int:
    #     dp_0, dp_1 = 0, float('-inf')
    #     for p in prices:
    #         tmp = dp_0
    #         dp_0 = max(dp_0, dp_1+p)
    #         dp_1 = max(dp_1, tmp-p)
    #     return dp_0

    def maxProfit(self, prices: List[int]) -> int:
        dp_0, dp_1 = 0, float('-inf')
        for p in prices:
            dp_0, dp_1 = max(dp_0, dp_1+p), max(dp_1, dp_0-p)
        return dp_0


s = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(prices))

prices = [1, 2, 3, 4, 5]
print(s.maxProfit(prices))
