# 买卖股票最大收益（只能买卖一次 leetcode 121, 次数不限 122，最多两次 123，最多 k 次 188）
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
    def maxProfit(self, k, prices):

        if k > len(prices)//2:  # 相当于有效的 k 取任意个，即次数不限
            dp_i0, dp_i1 = 0, float('-inf')
            for price in prices:
                dp_i0_old = dp_i0
                dp_i0 = max(dp_i0, dp_i1+price)
                dp_i1 = max(dp_i1, dp_i0_old-price)
            return dp_i0

        dp_ik0, dp_ik1 = [0]*(k+1), [float('-inf')]*(k+1)
        for price in prices:
            for j in range(1, k+1):
                dp_ik0[j] = max(dp_ik0[j], dp_ik1[j]+price)
                dp_ik1[j] = max(dp_ik1[j], dp_ik0[j-1]-price)
        return dp_ik0[k]


s = Solution()

# p = []
# print(s.maxProfit(p))

# p = [1, 2]
# print(s.maxProfit(p))
#
# p = [7,1,5,3,6,4]
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

# k 的测试数据
p = [2,4,1]
k = 2
print(s.maxProfit(k, p))

p = [3,2,6,5,0,3]
k = 2
print(s.maxProfit(k, p))