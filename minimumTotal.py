# 三角形最小路径和
class Solution:
    # def minimumTotal(self, triangle):
    #     if not triangle:
    #         return 0
    #     n = len(triangle)
    #     dp = [[0] * n for _ in range(n)]
    #
    #     dp[-1] = triangle[-1]
    #
    #     for i in range(n-2, -1, -1):
    #         for j in range(len(triangle[i])):
    #             dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
    #
    #     return dp[0][0]

    # 状态压缩
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        dp = triangle[-1]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

        return dp[0]

    # 不能使用 自顶向下，因为前面所选的最优不能导致最终最优的结果（相当于贪心选择），参考老师画的图
    # def minimumTotal(self, triangle):
    #     if not triangle:
    #         return 0
    #
    #     n = len(triangle)
    #     dp = [triangle[0][0]] * n
    #
    #     for i in range(1, n):
    #         for j in range(len(triangle[i])):
    #             dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
    #
    #     return dp[n-1]


s = Solution()
a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(s.minimumTotal(a))

