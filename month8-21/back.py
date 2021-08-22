# 0-1
class Solution:
    # def knapsack(self, weight, val, bag_v):
    #     n = len(weight)
    #     dp = [[0] * (bag_v+1) for _ in range(n)]
    #     for j in range(weight[0], bag_v+1):
    #         dp[0][j] = val[0]
    #
    #     for i in range(1, n):
    #         for j in range(bag_v+1):
    #             if j >= weight[i]:
    #                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+val[i])
    #             else:
    #                 dp[i][j] = dp[i - 1][j]
    #     return dp[n-1][bag_v]

    # def knapsack(self, weight, val, bag_v):
    #     n = len(weight)
    #     dp = [[0] * (bag_v+1) for _ in range(n+1)]
    #
    #     for i in range(1, n+1):
    #         for j in range(bag_v+1):
    #             if j >= weight[i-1]:
    #                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]]+val[i-1])
    #             else:
    #                 dp[i][j] = dp[i - 1][j]
    #
    #     return dp[n][bag_v]

    def knapsack(self, weight, val, bag_v):
        n = len(weight)
        dp = [0] * (bag_v+1)

        for i in range(n):
            for j in range(bag_v, weight[i]-1, -1):
                dp[j] = max(dp[j], dp[j-weight[i]]+val[i])

        return dp[-1]


s = Solution()
weight = [2, 3, 4, 5]
val = [3, 4, 5, 6]
bag_v = 8
print(s.knapsack(weight, val, bag_v))
