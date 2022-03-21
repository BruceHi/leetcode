# 1380. 矩阵中的幸运数
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        cols, res = [], []
        for row in matrix:
            cols.append(row.index(min(row)))
        for i, j in enumerate(cols):
            if matrix[i][j] == max(matrix[a][j] for a in range(len(matrix))):
                res.append(matrix[i][j])
        return res


s = Solution()
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(s.luckyNumbers(matrix))

matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(s.luckyNumbers(matrix))

matrix = [[7,8],[1,2]]
print(s.luckyNumbers(matrix))
