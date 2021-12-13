# 1034. 边界着色
from typing import List


class Solution:
    # 没理解题意
    # def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    #     m, n = len(grid), len(grid[0])
    #     record = grid[row][col]
    #     if record == color:
    #         return grid
    #
    #     def dfs(i, j):
    #         grid[i][j] = color
    #
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and grid[x][y] == record:
    #                 dfs(x, y)
    #
    #     dfs(row, col)
    #     if 0 < row < m-1 and 0 < col < n-1:
    #         grid[row][col] = record
    #     return grid

    # 失败
    # def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    #     m, n = len(grid), len(grid[0])
    #     record = grid[row][col]
    #     if record == color:
    #         return grid
    #
    #     not_border = []
    #     def dfs(i, j):
    #         grid[i][j] = color
    #
    #         count = 0
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n:
    #                 if grid[x][y] == record:
    #                     dfs(x, y)
    #                 if grid[x][y] == color:
    #                     count += 1
    #         if count == 4:
    #             not_border.append((i, j))
    #
    #     dfs(row, col)
    #     for i, j in not_border:
    #         grid[i][j] = record
    #     return grid


    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        raw = grid[row][col]
        if raw == color:
            return grid

        visited = [[False] * n for _ in range(m)]
        borders = []

        def dfs(i, j):
            visited[i][j] = True
            border = False
            for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                x, y = i + dx, j + dy
                if not (0 <= x < m and 0 <= y < n and grid[x][y] == raw):
                    border = True
                elif not visited[x][y]:
                    dfs(x, y)

            if border:
                borders.append((i, j))

        dfs(row, col)
        for i, j in borders:
            grid[i][j] = color
        return grid


s = Solution()
grid = [[1,1],[1,2]]
row = 0
col = 0
color = 3
print(s.colorBorder(grid, row, col, color))

grid = [[1,2,2],[2,3,2]]
row = 0
col = 1
color = 3
print(s.colorBorder(grid, row, col, color))

grid = [[1,1,1],[1,1,1],[1,1,1]]
row = 1
col = 1
color = 2
print(s.colorBorder(grid, row, col, color))

grid = [[1,2,1],[1,2,2],[2,2,1]]
row = 1
col = 1
color = 2
print(s.colorBorder(grid, row, col, color))

grid = [[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]]
row = 1
col = 3
color = 1
print(s.colorBorder(grid, row, col, color))
