# 买卖股票最大收益（只能买卖一次 leetcode 121, 次数不限 122，最多两次 123，最多 k 次 188）
from typing import List


class Solution:

    # # 只允许一次交易
    # def maxProfit(self, prices):
    #     min_price = float('inf')
    #     max_profit = 0
    #     for price in prices:
    #         min_price = min(min_price, price)  # 如果当前刚好是最低的，那么最大收益就要和0进行比较了。
    #         max_profit = max(max_profit, price - min_price)
    #     return max_profit

    # # 使用动态规划 不加入 k 的变化
    # def maxProfit(self, prices):
    #     if not prices:
    #         return 0
    #     n = len(prices)
    #     dp = [[0, 0] for _ in range(n)]  # 不能写成 dp = [[0, 0]] * n
    #     dp[-1][0], dp[-1][1] = 0, float('-inf')  # 不存在的情况用无穷表示，因为后面是求最大利益，所以用负无穷表示。
    #     for i in range(n):
    #         dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])  # 注意与交易多次的状态方程区别。
    #         dp[i][1] = max(dp[i-1][1], -prices[i])  # 只允许交易一次，说明买入前的最大利润是 0。
    #     return dp[n - 1][0]

    # 动态规划
    # def maxProfit(self, prices):
    #     dp_i0, dp_i1 = 0, float('-inf')
    #     for price in prices:
    #         dp_i0 = max(dp_i0, dp_i1+price)
    #         dp_i1 = max(dp_i1, -price)
    #     return dp_i0

    # ---------- 分割线 -----------------------------------------------------
    #
    # # 无数次买卖股票
    # def maxProfit(prices):
    #     max = 0
    #     for i in range(1, len(prices)):
    #         profit = prices[i] - prices[i - 1]
    #         if profit > 0:
    #             max += profit
    #     return max

    # # 使用动态规划，不加入 k 的变化
    # def maxProfit(self, prices):
    #     if not prices:
    #         return 0
    #     n = len(prices)
    #     if not n:
    #         return 0
    #     dp = [[0, 0] for _ in range(n)]  # 表示内部元素乘与 n,与 [0]*n 是一个效果， dp 存的都是可获得利益最大值
    #     dp[-1][0], dp[-1][1] = 0, float('-inf')  # 初始状态从 -1 就开始了，因为从 0 就可以进行选择了。
    #     for i in range(n):
    #         dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
    #         dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
    #     return dp[n-1][0]

    # def maxProfit(self, prices):
    #     dp_i0, dp_i1 = 0, float('-inf')
    #     for price in prices:
    #         tmp = dp_i0
    #         dp_i0 = max(dp_i0, dp_i1+price)
    #         dp_i1 = max(dp_i1, tmp-price)
    #     return dp_i0

    # ---------- 分割线 -----------------------------------------------------

    # # 最多两笔交易，动态规划，三维数组
    # def maxProfit(self, prices):
    #     if not prices:
    #         return 0
    #     n = len(prices)
    #     dp = [[[0, 0] for i in range(3)] for i in range(n)]  # 同样不能写成：# dp = [[[0, 0]] * 3] * n
    #
    #     for k in range(3):
    #         dp[0][k][1] = float('-inf')
    #         dp[-1][k][1] = float('-inf')
    #
    #     for i in range(n):
    #         for k in range(1, 3):
    #             dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])  # 注意与交易多次的状态方程区别。
    #             dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
    #     return dp[n-1][2][0]

    # def maxProfit(self, prices):
    #     dp_i10, dp_i11 = 0, float('-inf')
    #     dp_i20, dp_i21 = 0, float('-inf')
    #     for price in prices:
    #         dp_i20 = max(dp_i20, dp_i21 + price)
    #         dp_i21 = max(dp_i21, dp_i10 - price)
    #         dp_i10 = max(dp_i10, dp_i11+price)
    #         dp_i11 = max(dp_i11, -price)
    #     return dp_i20

    # ---------- 分割线 -----------------------------------------------------
    # 最多交易 k 次
    # def maxProfit(self, k, prices):
    #
    #     if k > len(prices)//2:  # 相当于有效的 k 取任意个，即次数不限
    #         dp_i0, dp_i1 = 0, float('-inf')
    #         for price in prices:
    #             dp_i0_old = dp_i0
    #             dp_i0 = max(dp_i0, dp_i1+price)
    #             dp_i1 = max(dp_i1, dp_i0_old-price)
    #         return dp_i0
    #
    #     dp_ik0, dp_ik1 = [0]*(k+1), [float('-inf')]*(k+1)
    #     for price in prices:
    #         for j in range(1, k+1):
    #             dp_ik0[j] = max(dp_ik0[j], dp_ik1[j]+price)
    #             dp_ik1[j] = max(dp_ik1[j], dp_ik0[j-1]-price)
    #     return dp_ik0[k]

    # # 一次买卖
    # def maxProfit(self, prices: List[int]) -> int:
    #     min_val = float('inf')
    #     res = 0
    #     for price in prices:
    #         min_val = min(min_val, price)
    #         res = max(res, price-min_val)
    #     return res

    # 多次买卖
    # def maxProfit(self, prices: List[int]) -> int:
    #     res = 0
    #     for i, price in enumerate(prices[:-1]):
    #         if prices[i+1] > price:
    #             res += prices[i+1] - price
    #     return res
    #

    # ------------------------------ 分割线 ------------------------------------------
    # 最多两次买卖
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices:
    #         return 0
    #     n = len(prices)
    #     dp = [[[0, 0] for _ in range(3)] for _ in range(n+1)]
    #
    #     # 第 0 天持有股票的，都是不可能的，所以设为 无穷小
    #     for j in range(3):
    #         dp[0][j][1] = float('-inf')
    #         dp[0][j][1] = float('-inf')
    #
    #     for i in range(1, n+1):
    #         for j in range(1, 3):
    #             dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
    #             dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])
    #     return dp[n][2][0]

    # # 状态压缩
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices:
    #         return 0
    #     n = len(prices)
    #     dp = [[0, 0] for _ in range(3)]
    #
    #     # 第 0 天持有股票的，都是不可能的，所以设为无穷小
    #     for j in range(3):
    #         dp[j][1] = float('-inf')
    #         dp[j][1] = float('-inf')
    #
    #     for i in range(1, n+1):
    #         for j in range(1, 3):
    #             # tmp = dp[j][0]
    #             dp[j][0] = max(dp[j][0], dp[j][1] + prices[i - 1])
    #             dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i - 1])
    #     return dp[2][0]

    # # 状态压缩
    # def maxProfit(self, prices: List[int]) -> int:
    #     dp_10, dp_11 = 0, float('-inf')
    #     dp_20, dp_21 = 0, float('-inf')
    #
    #     # 先写 dp_2 的就不用赋值给临时变量了。
    #     for price in prices:
    #         tmp = dp_10
    #         dp_10 = max(dp_10, dp_11 + price)
    #         dp_11 = max(dp_11, - price)
    #         dp_20 = max(dp_20, dp_21 + price)
    #         dp_21 = max(dp_21, tmp - price)
    #     return dp_20

    # def maxProfit(self, prices: List[int]) -> int:
    #     dp_i10, dp_i11 = 0, float('-inf')
    #     dp_i20, dp_i21 = 0, float('-inf')
    #     for price in prices:
    #         dp_i20 = max(dp_i20, dp_i21 + price)
    #         dp_i21 = max(dp_i21, dp_i10 - price)
    #         dp_i10 = max(dp_i10, dp_i11 + price)
    #         dp_i11 = max(dp_i11, - price)
    #     return dp_i20

    # # 拆分, 超时
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices:
    #         return 0
    #     n = len(prices)
    #     res = [0] * n  # 代表 i 左右两边最大收益之和
    #
    #     for i in range(n):
    #         min_val = float('inf')
    #         left_max, right_max = 0, 0
    #         for price in prices[:i]:
    #             min_val = min(min_val, price)
    #             left_max = max(left_max, price-min_val)
    #
    #         min_val = float('inf')
    #         for price in prices[i:]:
    #             min_val = min(min_val, price)
    #             right_max = max(right_max, price - min_val)
    #         res[i] = left_max + right_max
    #
    #     return max(res)

    # def maxProfit(self, prices: List[int]) -> int:
    #     buy_1, buy_2 = float('inf'), float('inf')
    #     pro_1, pro_2 = 0, 0  # profit
    #     for price in prices:
    #         buy_1 = min(buy_1, price)
    #         pro_1 = max(pro_1, price-buy_1)
    #         buy_2 = min(buy_2, price-pro_1)
    #         pro_2 = max(pro_2, price-buy_2)
    #     return pro_2

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k > len(prices) // 2:  # 相当于有效的 k 取任意个，即次数不限
            res = 0
            for i, price in enumerate(prices[:-1]):
                if prices[i+1] > price:
                    res += prices[i+1] - price
            return res

        dp_i0 = [0] * (k+1)
        dp_i1 = [float('-inf')] * (k+1)  # 0 天已经有一次交易了，这不可能

        for price in prices:
            for i in range(1, k+1):
                dp_i0[i] = max(dp_i0[i], dp_i1[i] + price)
                dp_i1[i] = max(dp_i1[i], dp_i0[i-1] - price)

        return dp_i0[k]


s = Solution()

# p = []
# print(s.maxProfit(p))
#
# p = [1]
# print(s.maxProfit(p))
#
# p = [1, 2]
# print(s.maxProfit(p))
#
# p = [7,1,5,3,6,4]
# print(s.maxProfit(p))
#
# p = [1,2,3,4,5]
# print(s.maxProfit(p))
#
# p = [7,6,4,3,1]
# print(s.maxProfit(p))
#
# # 最多两笔测试数据
# p = [3,3,5,0,0,3,1,4]
# print(s.maxProfit(p))
#
# p = [1,2,3,4,5]
# print(s.maxProfit(p))
#
# p = [1,2,4,2,5,7,2,4,9,0]
# print(s.maxProfit(p))

# k 的测试数据
p = [2,4,1]
k = 2
print(s.maxProfit(k, p))

p = [3,2,6,5,0,3]
k = 2
print(s.maxProfit(k, p))
