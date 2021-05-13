# 63. 不同路径 II
from typing import List


class Solution:
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     if obstacleGrid[0][0]:
    #         return 0
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     dp = [[0] * (n+1) for _ in range(m+1)]  # # dp(i,j) 表示到达横着第i个竖着第j个格子时不同路径个数。
    #
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if i == 1 and j == 1:
    #                 dp[1][1] = 1
    #                 continue
    #             if not obstacleGrid[i - 1][j - 1]:
    #                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #     return dp[m][n]


    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     if obstacleGrid[0][0]:
    #         return 0
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     dp = [[0] * n for _ in range(m)]  # dp(i,j) 表示到达坐标 （i,j）不同路径个数。
    #
    #     for i in range(m):
    #         if not obstacleGrid[i][0]:
    #             dp[i][0] = 1
    #         else:
    #             break
    #
    #     for j in range(n):
    #         if not obstacleGrid[0][j]:
    #             dp[0][j] = 1
    #         else:
    #             break
    #
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if not obstacleGrid[i][j]:
    #                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #     return dp[m-1][n-1]


    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     dp = [[0] * n for _ in range(m)]
    #
    #     for i in range(m):
    #         if not obstacleGrid[i][0]:
    #             dp[i][0] = 1
    #         else:
    #             break
    #
    #     for j in range(n):
    #         if not obstacleGrid[0][j]:
    #             dp[0][j] = 1
    #         else:
    #             break
    #
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if not obstacleGrid[i][j]:
    #                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #
    #     return dp[m-1][n-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if not obstacleGrid[i-1][j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]


s = Solution()
nmus = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(s.uniquePathsWithObstacles(nmus))

nmus = [
  [1]
]
print(s.uniquePathsWithObstacles(nmus))

obstacleGrid = [[0,1],[0,0]]
print(s.uniquePathsWithObstacles(obstacleGrid))
