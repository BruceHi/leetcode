# 892. 三维形体的表面积
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid)
        res = 0
        for i in range(m):
            for j in range(n):
                num = grid[i][j]
                if num != 0:
                    res += num * 6 - (num-1) * 2
                    if i-1 >= 0:
                        res -= min(grid[i-1][j], num) * 2
                    if j-1 >= 0:
                        res -= min(grid[i][j-1], num) * 2
        return res


s = Solution()
grid = [[2]]
print(s.surfaceArea(grid))

grid = [[1,2],[3,4]]
print(s.surfaceArea(grid))

grid = [[1,0],[0,2]]
print(s.surfaceArea(grid))

grid = [[1,1,1],[1,0,1],[1,1,1]]
print(s.surfaceArea(grid))

grid = [[2,2,2],[2,1,2],[2,2,2]]
print(s.surfaceArea(grid))
