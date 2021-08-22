# 最小路径和
from typing import List


class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     dp = [[float('inf')] * (n+1) for _ in range(m+1)]
    #     dp[0][1] = dp[1][0] = 0
    #
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
    #
    #     return dp[m][n]

    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     dp = [[float('inf')] * (n+1) for _ in range(m+1)]
    #     dp[0][1] = dp[1][0] = 0
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1]
    #     return dp[m][n]

    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     dp = [[float('inf')] * (n+1) for _ in range(m+1)]
    #     dp[0][1] = dp[1][0] = 0
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
    #     return dp[m][n]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]


s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(s.minPathSum(grid))

grid = [[1,2,3],[4,5,6]]
print(s.minPathSum(grid))

grid = [[5]]
print(s.minPathSum(grid))