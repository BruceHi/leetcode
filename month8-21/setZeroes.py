# 面试题 01.08. 零矩阵
from typing import List


class Solution:
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     row, col = set(), set()
    #     m, n = len(matrix), len(matrix[0])
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == 0:
    #                 row.add(i)
    #                 col.add(j)
    #
    #     for i in row:
    #         matrix[i] = [0] * n
    #     for j in col:
    #         for i in range(m):
    #             matrix[i][j] = 0

    # 使用 bool 数组
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0


s = Solution()
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
s.setZeroes(matrix)
print(matrix)

matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
s.setZeroes(matrix)
print(matrix)
