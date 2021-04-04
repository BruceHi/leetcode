# 73.矩阵置 0
from typing import List


class Solution:
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     row, col = set(), set()
    #     m, n = len(matrix), len(matrix[0])
    #     for i in range(m):
    #         for j in range(n):
    #             if not matrix[i][j]:
    #                 row.add(i)
    #                 col.add(j)
    #
    #     for i in row:
    #         matrix[i] = [0] * n
    #     for i in range(m):
    #         for j in col:
    #             matrix[i][j] = 0

    # 空间复杂度为 O(M+N)
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     rows, cols = set(), set()
    #     m, n = len(matrix), len(matrix[0])
    #     for i in range(m):
    #         for j in range(n):
    #             if not matrix[i][j]:
    #                 rows.add(i)
    #                 cols.add(j)
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if i in rows or j in cols:
    #                 matrix[i][j] = 0

    # 空间复杂度是 O(1)，利用第一行第一列标记某行某列有 0 的情况
    # 除此以外，还要注意第一行第一列可能有 0 的情况
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     m, n = len(matrix), len(matrix[0])
    #     flag_row = False
    #     flag_col = False
    #
    #     for j in range(n):
    #         if not matrix[0][j]:
    #             flag_row = True
    #             break
    #
    #     for i in range(m):
    #         if not matrix[i][0]:
    #             flag_col = True
    #             break
    #     # 标记
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if not matrix[i][j]:
    #                 matrix[0][j] = matrix[i][0] = 0
    #
    #     # 置 0
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if not matrix[i][0] or not matrix[0][j]:
    #                 matrix[i][j] = 0
    #
    #     if flag_row:
    #         matrix[0] = [0] * n
    #
    #     if flag_col:
    #         for i in range(m):
    #             matrix[i][0] = 0

    #-----------------分割线-------------------
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     m, n = len(matrix), len(matrix[0])
    #     row, col = set(), set()
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == 0:
    #                 row.add(i)
    #                 col.add(j)
    #     for i in row:
    #         matrix[i][:] = [0] * n
    #
    #     for i in range(m):
    #         for j in col:
    #             matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0


s = Solution()
nums = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
s.setZeroes(nums)
print(nums)

nums = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
s.setZeroes(nums)
print(nums)
