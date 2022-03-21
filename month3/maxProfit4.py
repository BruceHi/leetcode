# 188. 买卖股票的最佳时机4
# 最多运行交易 k 次
from typing import List


class Solution:
    # 动态规划
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    #     n = len(prices)
    #
    #     # 便于加快速度
    #     # if k >= n // 2:
    #     #     res = 0
    #     #     for i in range(n-1):
    #     #         if prices[i+1] > prices[i]:
    #     #             res += prices[i+1] - prices[i]
    #     #     return res
    #
    #     dp = [[[0, 0] for _ in range(k+1)] for _ in range(n+1)]
    #
    #     for j in range(k+1):
    #         dp[0][j][1] = float('-inf')
    #     for i in range(1, n+1):
    #         for j in range(1, k+1):
    #             dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i-1])
    #             dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i-1])
    #     return dp[n][k][0]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp_0, dp_1 = [0] * (k+1), [float('-inf')] * (k+1)
        for p in prices:
            for j in range(1, k+1):
                dp_0[j] = max(dp_0[j], dp_1[j]+p)
                dp_1[j] = max(dp_1[j], dp_0[j-1]-p)
        return dp_0[k]


s = Solution()
k = 2
prices = [2,4,1]
print(s.maxProfit(k, prices))

k = 2
prices = [3,2,6,5,0,3]
print(s.maxProfit(k, prices))

k = 2
prices = [3,3,5,0,0,3,1,4]
print(s.maxProfit(k, prices))  # 6
