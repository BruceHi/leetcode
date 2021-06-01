# 122.买卖股票的最佳时机2
# 允许交易多次
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res


s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))

prices = [1,2,3,4,5]
print(s.maxProfit(prices))
