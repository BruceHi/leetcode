# 240. 搜索二维矩阵 二
from bisect import bisect_left
from typing import List


class Solution:
    # 时间复杂度 O(m log n)，只用到了每行的元素从左到右升序排列这一个特征。
    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     n = len(matrix[0])
    #     for nums in matrix:
    #         if target < nums[0] or target > nums[-1]:
    #             continue
    #         idx = bisect_left(nums, target)
    #         if idx != n and nums[idx] == target:
    #             return True
    #     return False

    # # 按照对角线同时搜索行和列，时间复杂度为 O(log(n!))，时间复杂度看不懂
    # def searchMatrix(self, matrix, target):
    #
    #     def search(nums, target):
    #         idx = bisect_left(nums, target)
    #         if idx != len(nums) and nums[idx] == target:
    #             return True
    #         return False
    #
    #     if not matrix or not matrix[0]:
    #         return False
    #
    #     m, n = len(matrix), len(matrix[0])
    #     for i in range(min(m, n)):
    #         horizontal = search(matrix[i], target)
    #         ver_list = [matrix[a][i] for a in range(m)]
    #         vertical = search(ver_list, target)
    #         if horizontal or vertical:
    #             return True
    #     return False

    # 从左下角开始搜索，时间复杂度为 O(m + n)
    # def searchMatrix(self, matrix, target):
    #     if not matrix or not matrix[0]:
    #         return False
    #     m, n = len(matrix), len(matrix[0])
    #     x, y = m - 1, 0
    #     while x >= 0 and y < n:
    #         if target < matrix[x][y]:
    #             x -= 1
    #         elif target > matrix[x][y]:
    #             y += 1
    #         else:
    #             return True
    #     return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i >= 0 and j < n:
            if target == matrix[i][j]:
                return True
            if target > matrix[i][j]:
                j += 1
            else:
                i -= 1
        return False


s = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(s.searchMatrix(matrix, 5))

print(s.searchMatrix(matrix, 20))
