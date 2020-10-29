# 最长重复子数组, 连续的才叫子数组，不连续的叫子序列
from typing import List
from collections import Counter


class Solution:
    # def findLength(self, A: List[int], B: List[int]) -> int:
    #     n1, n2 = len(A), len(B)
    #     dp = [[0] * (n2+1) for _ in range(n1+1)]
    #     res = 0
    #     for i in range(1, n1+1):
    #         for j in range(1, n2+1):
    #             if A[i-1] == B[j-1]:
    #                 dp[i][j] = dp[i-1][j-1] + 1
    #                 res = max(res, dp[i][j])
    #     return res

    # # dp[i][j] 表示 A 的前 i 个字符与 B 的前 j 个字符公共的、长度最长的子数组的长度。
    # # A[i-1] 表示 A 的第 i 个字符。
    # def findLength(self, A: List[int], B: List[int]) -> int:
    #     m, n = len(A), len(B)
    #     dp = [[0] * (n+1) for _ in range(m+1)]
    #
    #     res = 0
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if A[i-1] == B[j-1]:
    #                 dp[i][j] = dp[i-1][j-1] + 1
    #                 res = max(res, dp[i][j])
    #     return res

    # 令 dp[i][j] 表示 A[i:] 和 B[j:] 的最长公共前缀，那么答案即为所有 dp[i][j] 中的最大值。
    # 如果 A[i] == B[j]，那么 dp[i][j] = dp[i + 1][j + 1] + 1，否则 dp[i][j] = 0。
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0] * (n+1) for _ in range(m+1)]

        res = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    res = max(res, dp[i][j])
        return res


s = Solution()
A = [1,2,3,2,1]
B = [3,2,1,4,7]
print(s.findLength(A, B))

A = [0,0,0,0,1]
B = [1,0,0,0,0]
print(s.findLength(A, B))

A = [0,0,0,0,0]
B = [0,0,0,0,0]
print(s.findLength(A, B))
