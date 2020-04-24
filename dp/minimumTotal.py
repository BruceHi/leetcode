# 三角形最小路径和
class Solution:
    # 前两中方法都是自下而上分析
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

    # # 自顶向下，可以复用 triangle。
    # def minimumTotal(self, triangle):
    #     if not triangle:
    #         return 0
    #
    #     n = len(triangle)
    #
    #     dp = [[0] * n for _ in range(n)]
    #     dp[0][0] = triangle[0][0]
    #
    #     for i in range(1, n):
    #         for j in range(len(triangle[i])):
    #             if j == 0:
    #                 dp[i][j] = dp[i-1][j] + triangle[i][j]
    #             elif j == len(triangle[i])-1:
    #                 dp[i][j] = dp[i-1][j-1] + triangle[i][j]
    #             else:
    #                 dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    #
    #     return min(dp[n-1])  # 最后需要特殊处理的，比如求最大值、最小值，都不能使用状态压缩

    # 自顶向下，复用 triangle。
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        n = len(triangle)

        for i in range(1, n):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]

        return min(triangle[n - 1])


s = Solution()
a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(s.minimumTotal(a))

