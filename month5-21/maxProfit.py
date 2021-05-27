# 121. 买卖股票的最佳时期
# 只允许交易一次
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = float('inf')
        for p in prices:
            if p < min_price:
                min_price = p
            res = max(res, p-min_price)
        return res


s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))

prices = [7,6,4,3,1]
print(s.maxProfit(prices))
