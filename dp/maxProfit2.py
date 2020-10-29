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

    # # 有手续费
    # def maxProfit(self, prices, fee):
    #     dp_i0, dp_i1 = 0, float('-inf')
    #     for price in prices:
    #         dp_i0_old = dp_i0
    #         dp_i0 = max(dp_i0, dp_i1+price)
    #         dp_i1 = max(dp_i1, dp_i0_old-price-fee)
    #     return dp_i0

    # 有手续费 i0：第 i 天没有，i1 第 i 天持有。买入的时候扣手续费。
    # def maxProfit(self, prices, fee):
    #     dp_i0, dp_i1 = 0, float('-inf')
    #     for price in prices:
    #         dp_i0, dp_i1 = max(dp_i0, dp_i1+price), max(dp_i1, dp_i0-price-fee)
    #     return dp_i0

    def maxProfit(self, prices, fee):
        cash, hold = 0, float('-inf')
        for price in prices:
            cash, hold = max(cash, hold+price), max(hold, cash-price-fee)
        return cash


s = Solution()

# p = [1,2,3,0,2]
# print(s.maxProfit(p))
#
# p = [1, 2]
# print(s.maxProfit(p))

prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(s.maxProfit(prices, fee))
