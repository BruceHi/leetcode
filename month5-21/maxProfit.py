# 121. 买卖股票的最佳时期
# 只允许交易一次
from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     res = 0
    #     min_price = float('inf')
    #     for p in prices:
    #         if p < min_price:
    #             min_price = p
    #         res = max(res, p-min_price)
    #     return res

    # def maxProfit(self, prices: List[int]) -> int:
    #     res = 0
    #     min_price = float('inf')
    #     for price in prices:
    #         if price < min_price:
    #             min_price = price
    #         res = max(res, price-min_price)
    #     return res

    # 常规解法
    # def maxProfit(self, prices: List[int]) -> int:
    #     res = 0
    #     min_p = float('inf')
    #     for p in prices:
    #         min_p = min(min_p, p)
    #         res = max(res, p-min_p)
    #     return res

    # 动态规划
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     dp = [[0, 0] for _ in range(n+1)]
    #
    #     dp[0][1] = float('-inf')
    #     for i in range(1, n+1):
    #         dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
    #         dp[i][1] = max(dp[i-1][1], -prices[i-1])
    #     return dp[n][0]

    # 状态压缩
    def maxProfit(self, prices: List[int]) -> int:
        dp_0, dp_1 = 0, float('-inf')
        for p in prices:
            dp_0 = max(dp_0, dp_1+p)
            dp_1 = max(dp_1, -p)
        return dp_0


s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))

prices = [7,6,4,3,1]
print(s.maxProfit(prices))
