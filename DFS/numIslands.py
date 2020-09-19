# 岛屿的个数
from typing import List


# 回溯
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]:
#             return 0
#         count = 0
#         m, n = len(grid), len(grid[0])
#
#         def DFS(i, j):
#             grid[i][j] = '0'
#             for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#                 x, y = i+dx, j+dy
#                 if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
#                     DFS(x, y)
#
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     count += 1
#                     DFS(i, j)
#
#         return count

# 并查集
# class UnionFind:
#     def __init__(self, grid):
#         m, n = len(grid), len(grid[0])
#         self.count = 0
#         self.parent = [-1] * (m * n)
#         self.rank = [0] * (m * n)
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     self.parent[i * n + j] = i * n + j
#                     self.count += 1
#
#     # 查找时路径压缩
#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])  # 以保证所有结点都指向根节点。
#         return self.parent[i]
#
#     # 按 rank 合并
#     def union(self, x, y):
#         rootx = self.find(x)
#         rooty = self.find(y)
#         if rootx != rooty:
#             if self.rank[rootx] < self.rank[rooty]:
#                 self.parent[rootx] = rooty
#             elif self.rank[rootx] > self.rank[rooty]:
#                 self.parent[rooty] = rootx
#             else:
#                 self.parent[rooty] = rootx
#                 self.rank[rootx] += 1
#             self.count -= 1


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]:
#             return 0
#         uf = UnionFind(grid)
#         m, n = len(grid), len(grid[0])
#
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':  # 先不染色看看
#                     grid[i][j] = '0'  # 染色能够减少大量 union 判断。以保证合并的都是没有出现的数据。
#                     for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
#                         if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
#                             uf.union(i*n+j, x*n+y)
#
#         return uf.count

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#
#         def dfs(row, col):
#             grid[row][col] = '0'
#             for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
#                 x, y = row + dx, col + dy
#                 if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
#                     dfs(x, y)
#
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':  # 里面类型都是 str 类型，要特别注意。
#                     count += 1
#                     dfs(i, j)
#
#         return count


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.parent = [-1] * (m * n)  # 若赋值为 0 , 则默认第0位的父节点为 0 了。
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:  # 注意这是个 if 语句，不是循环语句，目的是为了找到 i 的顶头上司
            self.parent[i] = self.find(self.parent[i])  # 其结果并不是 self.parent[i] == i，才退出。
        return self.parent[i]

    def union(self, x, y):
        if self.find(x) != self.find(y):
            rootx, rooty = self.find(x), self.find(y)
            self.parent[rootx] = rooty
            self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        uf = UnionFind(grid)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            uf.union(i * n + j, x * n + y)
        return uf.count


s = Solution()
a = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(s.numIslands(a))

a = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(s.numIslands(a))

a = []
print(s.numIslands(a))

a = [["1"], ["1"]]
print(s.numIslands(a))

a = [["1","1"]]
print(s.numIslands(a))

a = [["1","1","1"],["1","0","1"],["1","1","1"]]
print(s.numIslands(a))
