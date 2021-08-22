# 62. 不同路径
# 还可以用排列组合，打扰了
class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[1] * n for _ in range(m)]
    #
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #
    #     return dp[m-1][n-1]

    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [1] * n
    #
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[j] += dp[j-1]
    #
    #     return dp[n-1]

    # 注意条件 m>=1，n>=1
    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[0] * (n+1) for _ in range(m+1)]
    #     dp[1][1] = 1
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if i != 1 or j != 1:
    #                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #     return dp[m][n]

    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[1] * n for _ in range(m)]
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #     return dp[m-1][n-1]

    # 路径压缩
    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [1] + [0] * (n-1)
    #     for _ in range(m):
    #         for j in range(1, n):
    #             dp[j] += dp[j-1]
    #     return dp[-1]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]


s = Solution()
m = 3
n = 2
print(s.uniquePaths(m, n))

m = 7
n = 3
print(s.uniquePaths(m, n))

m = 3
n = 7
print(s.uniquePaths(m, n))