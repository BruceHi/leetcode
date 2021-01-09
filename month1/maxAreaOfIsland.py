# 695. 岛屿的最大面积
from typing import List


class Solution:
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #
    #     def dfs(i, j):
    #         grid[i][j] = 0
    #         nonlocal count
    #         count += 1
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and grid[x][y]:
    #                 dfs(x, y)
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j]:
    #                 count = 0
    #                 dfs(i, j)
    #                 res = max(res, count)
    #     return res

    # 有返回值的深度优先搜索，更直观
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = 0
            count = 1
            for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    count += dfs(x, y)
            return count

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, dfs(i, j))
        return res


s = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(s.maxAreaOfIsland(grid))

grid = [[0,0,0,0,0,0,0,0]]
print(s.maxAreaOfIsland(grid))
