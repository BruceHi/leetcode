# 岛屿的周长
from typing import List

class Solution:
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j]:
    #                 for x, y in zip([1, -1, 0, 0], [0, 0, 1, -1]):
    #                     if i + x == -1 or i + x == m:
    #                         res += 1
    #                     elif j + y == -1 or j + y == n:
    #                         res += 1
    #                     elif not grid[i+x][j+y]:
    #                         res += 1
    #     return res

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                        x, y = i + dx, j + dy
                        if x < 0 or y < 0 or x == m or y == n or not grid[x][y]:
                            res += 1
        return res



s = Solution()
grid = [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]
print(s.islandPerimeter(grid))
