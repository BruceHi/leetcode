from typing import List


class Solution:
    # 超时，分别计算出2个矩阵的岛屿，然后遍历第2个岛屿是否是第一个岛屿的子集
    # def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    #
    #     def get_res(grid):
    #         res = []
    #         m, n = len(grid), len(grid[0])
    #
    #         def dfs(i, j):
    #             grid[i][j] = 0
    #             cur = {(i, j)}
    #             for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #                 x, y = i + dx, j + dy
    #                 if 0 <= x < m and 0 <= y < n and grid[x][y]:
    #                     cur.update(dfs(x, y))
    #             return cur
    #
    #         for i in range(m):
    #             for j in range(n):
    #                 if grid[i][j]:
    #                     res.append(dfs(i, j))
    #         return res
    #     res1 = get_res(grid1)
    #     res2 = get_res(grid2)
    #
    #     count = 0
    #     for a in res2:
    #         for b in res1:
    #             if a | b == b:
    #                 count += 1
    #     return count

    # def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    #     m, n = len(grid1), len(grid1[0])
    #
    #     def get_island(grid):
    #
    #         def dfs(i, j):
    #             grid[i][j] = 0
    #             cur = [(i, j)]
    #             for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #                 x, y = i + dx, j + dy
    #                 if 0 <= x < m and 0 <= y < n and grid[x][y]:
    #                     cur += dfs(x, y)
    #             return cur
    #
    #         res = []
    #         for i in range(m):
    #             for j in range(n):
    #                 if grid[i][j]:
    #                     res.append(dfs(i, j))
    #         return res
    #
    #     nums = get_island(grid2)
    #     print(nums)

    # 依旧超时：计算第二个岛屿的索引值，然后一计算出来一批岛屿就进行判定。
    # 使用染色法
    # def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    #     m, n = len(grid1), len(grid1[0])
    #
    #     def dfs(i, j):
    #         grid2[i][j] = 0
    #         cur = [(i, j)]
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and grid2[x][y]:
    #                 cur += dfs(x, y)
    #         return cur
    #
    #     count = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid2[i][j]:
    #                 nums = dfs(i, j)
    #                 if all(map(lambda x: grid1[x[0]][x[1]], nums)):
    #                     count += 1
    #     return count
    #

    # 成功
    # def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    #     m, n = len(grid1), len(grid1[0])
    #
    #     def dfs(i, j):
    #         grid2[i][j] = 0
    #         island = True
    #         if not grid1[i][j]:
    #             island = False
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and grid2[x][y]:
    #                 island &= dfs(x, y)
    #         return island
    #
    #     count = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid2[i][j]:
    #                 count += dfs(i, j)
    #     return count


    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        def dfs(i, j):
            grid2[i][j] = 0
            island = grid1[i][j]  # 模拟 False
            for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and grid2[x][y]:
                    island &= dfs(x, y)
            return island

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    count += dfs(i, j)
        return count


s = Solution()
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
print(s.countSubIslands(grid1, grid2))

grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
print(s.countSubIslands(grid1, grid2))

print({(1, 2)} | {(1, 2), (2, 3)} == {(1, 2), (2, 3)})
print(True & False)
