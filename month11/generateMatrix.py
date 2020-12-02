# 59. 螺旋矩阵2
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        matrix = [[0] * n for _ in range(n)]
        num, target = 1, n * n
        while num <= target:
            for i in range(l, r + 1):
                matrix[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1):
                matrix[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):
                matrix[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1):
                matrix[i][l] = num
                num += 1
            l += 1
        return matrix


s = Solution()
print(s.generateMatrix(3))
