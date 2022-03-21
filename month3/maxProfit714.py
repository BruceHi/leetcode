# 714. 买卖股票的最佳时期含手续费
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_0, dp_1 = 0, float('-inf')
        for p in prices:
            dp_0, dp_1 = max(dp_0, dp_1+p-fee), max(dp_1, dp_0-p)
        return dp_0


s = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(s.maxProfit(prices, fee))

prices = [1,3,7,5,10,3]
fee = 3
print(s.maxProfit(prices, fee))
