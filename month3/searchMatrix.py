# 74. 搜索二维矩阵
from typing import List


class Solution:
    # # 从左下角搜索
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     m, n = len(matrix), len(matrix[0])
    #     i, j = m-1, 0
    #     while i >= 0 and j < n:
    #         if target < matrix[i][j]:
    #             i -= 1
    #         elif target > matrix[i][j]:
    #             j += 1
    #         else:
    #             return True
    #     return False

    # 二分搜索
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     m, n = len(matrix), len(matrix[0])
    #     left, right = 0, m*n - 1
    #     while left <= right:
    #         mid = left + right >> 1
    #         val = matrix[mid // n][mid % n]
    #         if val == target:
    #             return True
    #         if val < target:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return False

    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     m, n = len(matrix), len(matrix[0])
    #     left, right = 0, m * n - 1
    #     while left <= right:
    #         mid = left + right >> 1
    #         num = matrix[mid // n][mid % n]
    #         if num == target:
    #             return True
    #         if num < target:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n - 1
        while left <= right:
            mid = left + right >> 1
            val = matrix[mid // n][mid % n]
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return True
        return False



s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(s.searchMatrix(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(s.searchMatrix(matrix, target))

matrix = [[1]]
target = 0
print(s.searchMatrix(matrix, target))
