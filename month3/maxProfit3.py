# 123. 买卖股票的最佳时机3
# 最多允许两次
from typing import List


class Solution:
    # 动态压缩
    # def maxProfit(self, prices: List[int]) -> int:
    #     dp_0, dp_1 = [0] * 3, [float('-inf')] * 3
    #     for p in prices:
    #         for j in range(1, 3):
    #             dp_0[j] = max(dp_0[j], dp_1[j]+p)
    #             dp_1[j] = max(dp_1[j], dp_0[j-1]-p)
    #     return dp_0[2]

    def maxProfit(self, prices: List[int]) -> int:
        dp_1_0, dp_2_0 = 0, 0  # dp_k_（有无）
        dp_1_1, dp_2_1 = float('-inf'), float('-inf')
        for p in prices:
            tmp2 = dp_1_0
            dp_1_0 = max(dp_1_0, dp_1_1 + p)
            dp_2_0 = max(dp_2_0, dp_2_1 + p)
            dp_1_1 = max(dp_1_1, -p)  # 首次情况
            dp_2_1 = max(dp_2_1, tmp2 - p)
        return dp_2_0


s = Solution()
prices = [3,3,5,0,0,3,1,4]
print(s.maxProfit(prices))

prices = [1,2,3,4,5]
print(s.maxProfit(prices))

prices = [7,6,4,3,1]
print(s.maxProfit(prices))

prices = [1]
print(s.maxProfit(prices))
