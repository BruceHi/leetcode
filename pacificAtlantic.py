# 417. 太平洋大西洋水流问题
from typing import List


class Solution:
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     m, n = len(heights), len(heights[0])
    #     res = set()
    #     memo_p, memo_a = set(), set()
    #
    #     # for i in range(m):
    #     #     memo_p.add((i, 0))
    #     # for j in range(n):
    #     #     memo_p.add((0, j))
    #
    #     # 先太平洋问题
    #     def dfs(i, j):
    #         res.add((i, j))
    #         for dx, dy in zip([0, 1], [1, 0]):
    #             x, y = i + dx, j + dy
    #             if x < m and y < n and heights[x][y] >= heights[i][j]:
    #                 dfs(x, y)
    #
    #     for i in range(m):
    #         dfs(i, 0)
    #     for j in range(1, n):
    #         dfs(0, j)
    #     a = res
    #
    #
    #     res = set()
    #     def dfs(i, j):
    #         res.add((i, j))
    #         for dx, dy in zip([-1, 0], [0, -1]):
    #             x, y = i + dx, j + dy
    #             if x < m and y < n and heights[x][y] >= heights[i][j]:
    #                 dfs(x, y)
    #
    #     for i in range(m):
    #         dfs(i, n-1)
    #     for j in range(n):
    #         dfs(m-1, j)
    #     b = res
    #
    #     return sorted(a & b)

    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     m, n = len(heights), len(heights[0])
    #
    #     res = set()
    #     memo = set()
    #     # 先太平洋问题
    #     def dfs(i, j):
    #         if (i, j) in memo:
    #             return
    #         res.add((i, j))
    #         memo.add((i, j))
    #         for dx, dy in zip([0, 1], [1, 0]):
    #             x, y = i + dx, j + dy
    #             if x < m and y < n and heights[x][y] >= heights[i][j]:
    #                 dfs(x, y)
    #
    #     for i in range(m):
    #         dfs(i, 0)
    #     for j in range(1, n):
    #         dfs(0, j)
    #     a = res
    #
    #     res = set()
    #     memo = set()
    #     def dfs(i, j):
    #         if (i, j) in memo:
    #             return
    #         res.add((i, j))
    #         memo.add((i, j))
    #         for dx, dy in zip([-1, 0], [0, -1]):
    #             x, y = i + dx, j + dy
    #             if x < m and y < n and heights[x][y] >= heights[i][j]:
    #                 dfs(x, y)
    #
    #     for i in range(m):
    #         dfs(i, n-1)
    #     for j in range(n):
    #         dfs(m-1, j)
    #     b = res
    #
    #     return list(map(list, a & b))

    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     m, n = len(heights), len(heights[0])
    #
    #     def dfs(i, j, memo):
    #         if (i, j) in memo:
    #             return
    #         res.add((i, j))
    #         memo.add((i, j))
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
    #                 dfs(x, y, memo)
    #
    #     # 太平洋
    #     res = set()
    #     diff = [[0, 1], [1, 0]]
    #     for i in range(m):
    #         dfs(i, 0, set())
    #     for j in range(1, n):
    #         dfs(0, j, set())
    #     a = res
    #     # print(a)
    #     # 大西洋 可能各个方向，不一定要左上
    #     res = set()
    #     diff = [[0, -1], [-1, 0]]
    #     for i in range(m):
    #         dfs(i, n-1, set())
    #     for j in range(n):  # 左上的时候，这里也要改
    #         dfs(m-1, j, set())
    #     b = res
    #     # print(b)
    #     return list(map(list, a & b))

    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     m, n = len(heights), len(heights[0])
    #
    #     def search(starts):
    #         visited = set()  # 既是访问过的，也是结果上的
    #
    #         def dfs(i, j):
    #             if (i, j) in visited:
    #                 return
    #             visited.add((i, j))
    #             for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #                 x, y = i + dx, j + dy
    #                 if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
    #                     dfs(x, y)
    #
    #         for i, j in starts:
    #             dfs(i, j)
    #         return visited
    #
    #     p = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
    #     a = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]
    #     return list(map(list, search(p) & search(a)))

    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     m, n = len(heights), len(heights[0])
    #
    #     def search(starts):
    #         visited = set()
    #
    #         def dfs(i, j):
    #             if (i, j) in visited:
    #                 return
    #             visited.add((i, j))
    #             for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #                 x, y = i + dx, j + dy
    #                 if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
    #                     dfs(x, y)
    #
    #         for i, j in starts:
    #             dfs(i, j)
    #         return visited
    #
    #     p = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
    #     a = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]
    #     return list(map(list, search(p) & search(a)))

    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     m, n = len(heights), len(heights[0])
    #
    #     def search(starts):
    #         visited = set()
    #
    #         def dfs(i, j):
    #             if (i, j) in visited:
    #                 return
    #             visited.add((i, j))
    #             for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #                 x, y = i + dx, j + dy
    #                 if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
    #                     dfs(x, y)
    #
    #         for i, j in starts:
    #             dfs(i, j)
    #         return visited
    #
    #     p = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
    #     a = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]
    #     return list(map(list, search(p) & search(a)))

    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     m, n = len(heights), len(heights[0])
    #
    #     def search(starts):
    #         res = set()
    #
    #         def dfs(i, j):
    #             if (i, j) in res:
    #                 return
    #             res.add((i, j))
    #
    #             for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #                 x, y = i + dx, j + dy
    #                 if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
    #                     dfs(x, y)
    #
    #         for i, j in starts:
    #             dfs(i, j)
    #         return res
    #
    #     p_box = [(0, y) for y in range(n)] + [(x, 0) for x in range(m)]
    #     a_box = [(m-1, y) for y in range(n)] + [(x, n-1) for x in range(m)]
    #
    #     return list(map(list, search(p_box) & search(a_box)))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def search(start):
            res = set()

            def dfs(i, j):
                if (i, j) in res:
                    return
                res.add((i, j))

                for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
                        dfs(x, y)

            for i, j in start:
                dfs(i, j)
            return res

        p = [[0, y] for y in range(n)] + [[x, 0] for x in range(m)]
        a = [[m-1, y] for y in range(n)] + [[x, n-1] for x in range(m)]
        return list(map(list, search(p) & search(a)))





s = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(s.pacificAtlantic(heights))

heights = [[2,1],[1,2]]
print(s.pacificAtlantic(heights))

heights = [[1]]
print(s.pacificAtlantic(heights))

heights = [[1,2,3],[8,9,4],[7,6,5]]
print(s.pacificAtlantic(heights))

heights = [[1,1],[1,1],[1,1]]
print(s.pacificAtlantic(heights))
