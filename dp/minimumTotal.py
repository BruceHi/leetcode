# 三角形最小路径和
from typing import List


class Solution:

    # 自顶向下
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     dp = [[float('inf')] * n for _ in range(n)]
    #
    #     dp[0][0] = triangle[0][0]
    #     for i in range(1, n):
    #         dp[i][0] = dp[i-1][0] + triangle[i][0]
    #
    #     for i in range(1, n):
    #         for j in range(1, i+1):
    #             dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
    #
    #     return int(min(dp[n-1]))

    # # 从底向上，压缩路径
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     dp = triangle[-1]
    #     for i in range(len(triangle)-2, -1, -1):
    #         for j in range(len(triangle[i])):
    #             dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
    #     return dp[0]

    # 自顶向下，空间复用 triangle
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     for i in range(1, len(triangle)):
    #         triangle[i][0] += triangle[i-1][0]
    #         for j in range(1, i):
    #             triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
    #         triangle[i][i] += triangle[i-1][i-1]
    #     return min(triangle[len(triangle) - 1])


    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     dp = [[0] * n for _ in range(n)]
    #     dp[-1] = triangle[-1]
    #     for i in range(n-2, -1, -1):
    #         for j in range(i+1):
    #             dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
    #     return dp[0][0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle), len(triangle[-1])
        dp = [[0] * n for _ in range(m)]

        dp[-1] = triangle[-1]

        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]


s = Solution()
a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(s.minimumTotal(a))

triangle = [[-10]]
print(s.minimumTotal(triangle))
