# 股票交易
class Solution:
    # 有冷冻期，即卖出股票后第二天无法买入股票。
    # def maxProfit(self, prices):
    #     dp_i0, dp_i1 = 0, float('-inf')
    #     dp_i0_pre = 0  # 相当于dp(i-1, 0)
    #     for price in prices:
    #         dp_i0_old = dp_i0  # 相当于 dp(i-1,0)
    #         dp_i0 = max(dp_i0, dp_i1+price)
    #         dp_i1 = max(dp_i1, dp_i0_pre-price)  # 经过一轮循环后：dp_i1 就是 dp(i+1, 1)，与 pre 差值为 2。
    #         dp_i0_pre = dp_i0_old
    #     return dp_i0

    # 有手续费
    def maxProfit(self, prices, fee):
        dp_i0, dp_i1 = 0, float('-inf')
        for price in prices:
            dp_i0_old = dp_i0
            dp_i0 = max(dp_i0, dp_i1+price)
            dp_i1 = max(dp_i1, dp_i0_old-price-fee)
        return dp_i0


s = Solution()

# p = [1,2,3,0,2]
# print(s.maxProfit(p))
#
# p = [1, 2]
# print(s.maxProfit(p))

prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(s.maxProfit(prices, fee))