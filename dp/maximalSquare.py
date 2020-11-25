# 221. 最大正方形
from typing import List


class Solution:
    # 错误
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #
    #     def dfs(i, j, edge):
    #         # pass
    #         if i == m - 1 or j == n - 1:
    #             return edge
    #
    #         for dx, dy in ([0, 1], [1, 0], [0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] == '0':
    #                 return edge
    #
    #         for dx, dy in ([0, 1], [1, 0], [0, 0]):
    #             x, y = i + dx, j + dy
    #             return dfs(x, y, edge+1)
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == '1':
    #                 res = max(res, dfs(i, j, 1))
    #     return res

    # # 回溯法
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     if not matrix:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])
    #
    #     def dfs(i, j, edge):
    #         # pass
    #         if i + edge == m or j + edge == n:
    #             return edge
    #
    #         x, y = i + edge, j + edge
    #         for a in range(i, x+1):
    #             if matrix[a][y] == '0':
    #                 return edge
    #
    #         for b in range(j, y+1):
    #             if matrix[x][b] == '0':
    #                 return edge
    #         return dfs(i, j, edge+1)
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == '1':
    #                 res = max(res, dfs(i, j, 1))
    #     return res * res


    # 动态规划，dp(i,j) 表示以（i, j）为右下角，只含 1 的正方形边长的最大值。
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if not i or not j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                res = max(res, dp[i][j])
        return res ** 2





s = Solution()
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

print(s.maximalSquare(matrix))

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","1","1","1"]]

print(s.maximalSquare(matrix))

matrix = [["1","1"],
          ["1","1"]]

print(s.maximalSquare(matrix))

matrix = [["1","1", '1'],
          ["1","1", '1'],
          ['1','1','0']]

print(s.maximalSquare(matrix))

matrix = [['1']]

print(s.maximalSquare(matrix))

matrix = [['0']]

print(s.maximalSquare(matrix))

matrix = []

print(s.maximalSquare(matrix))