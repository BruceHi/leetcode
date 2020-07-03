# 最长重复子数组, 连续的才叫子数组，不连续的叫子序列
from typing import List
from collections import Counter


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n1, n2 = len(A), len(B)
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        res = 0
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
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
