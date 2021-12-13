# 807. 保持城市边际线
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = list(map(max, grid))
        col_max = list(map(max, zip(*grid)))
        n = len(grid)
        res = 0
        for i in range(n):
            for j in range(n):
                res += min(row_max[i], col_max[j]) - grid[i][j]
        return res


s = Solution()
grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
print(s.maxIncreaseKeepingSkyline(grid))

grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(s.maxIncreaseKeepingSkyline(grid))
