# 剑指 offer 04. 二维数组中的查找
# 与 240. 搜索二维矩阵 II searchMatrix 一样
from typing import List


class Solution:
    # def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
    #     if not matrix:
    #         return False
    #     m, n = len(matrix), len(matrix[0])
    #     i, j = m-1, 0
    #     # while 0 <= i < m and 0 <= j < n:
    #     while i >= 0 and j < n:  # 不用完整的判定
    #         if matrix[i][j] < target:
    #             j += 1
    #         elif matrix[i][j] > target:
    #             i -= 1
    #         else:
    #             return True
    #     return False

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i >= 0 and j < n:
            if target < matrix[i][j]:
                i -= 1
            elif target > matrix[i][j]:
                j += 1
            else:
                return True
        return False


s = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(s.findNumberIn2DArray(matrix, target=5))
print(s.findNumberIn2DArray(matrix, target=20))

print(s.findNumberIn2DArray([[]], target=20))
