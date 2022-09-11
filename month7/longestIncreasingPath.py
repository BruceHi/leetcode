# 329. 矩阵中的最长递增路径
# 有向图中的最长路径
from typing import List
from functools import lru_cache


class Solution:

    # # # 回溯法
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     if not matrix:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])
    #
    #     @lru_cache(None)  # 使用装饰器，缓存临时变量
    #     def dfs(i, j):
    #         best = 1
    #         for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 best = max(best, dfs(x, y) + 1)
    #         return best
    #
    #     #  dfs = lru_cache(None)(dfs)  # 或这样写
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             res = max(res, dfs(i, j))
    #     return res

    # # 回溯法  缓存验证
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     if not matrix:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])
    #
    #     # @lru_cache(None)  # 缓存临时变量
    #     def dfs(i, j):
    #         best = 1
    #         for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 best = max(best, dfs(x, y) + 1)
    #         print('运行了')
    #         print('缓存 dfs(%d, %d) = %d' % (i, j, best))
    #         return best
    #
    #     # res = 0
    #     # for i in range(m):
    #     #     for j in range(n):
    #     #         res = max(res, dfs(i, j))
    #     # return res
    #
    #     dfs = lru_cache(None)(dfs)
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             print(dfs(i, j))
    #     return res

    # 记忆化
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     if not matrix:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])
    #     record = [[0] * n for _ in range(m)]
    #     res = 0
    #
    #     def dfs(i, j):
    #         nonlocal res
    #         compare = []
    #         for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 if record[x][y]:
    #                     compare.append(record[x][y])
    #                 else:
    #                     compare.append(dfs(x, y))
    #         record[i][j] = max(compare) + 1 if compare else 1
    #         res = max(res, record[i][j])
    #         return record[i][j]
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if not record[i][j]:
    #                 dfs(i, j)
    #
    #     return res

    # # 记忆化
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     if not matrix:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])
    #     memo = [[0] * n for _ in range(m)]
    #
    #     def dfs(i, j):  # memo[i][j] 里面存储的就是 dfs(i, j) 的值
    #         if memo[i][j]:
    #             return memo[i][j]
    #         memo[i][j] = 1
    #         for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 memo[i][j] = max(memo[i][j], dfs(x, y)+1)
    #         return memo[i][j]
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             res = max(res, dfs(i, j))
    #
    #     return res

    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     if not matrix:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])
    #     memo = [[0] * n for _ in range(m)]
    #
    #     def dfs(i, j):
    #         if memo[i][j]:
    #             return memo[i][j]
    #         memo[i][j] = 1
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 memo[i][j] = max(memo[i][j], dfs(x, y) + 1)
    #         return memo[i][j]
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             res = max(res, dfs(i, j))
    #     return res

    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     if not matrix:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])
    #     res = 0
    #
    #     @lru_cache(None)
    #     def dfs(i, j):
    #         best = 1
    #         nonlocal res
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 best = max(best, dfs(x, y) + 1)
    #         res = max(res, best)
    #         return best
    #
    #     for i in range(m):
    #         for j in range(n):
    #             dfs(i, j)
    #     return res

    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #     res = 0
    #
    #     @lru_cache(None)
    #     def dfs(i, j):
    #         best = 1
    #         nonlocal res
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 best = max(best, dfs(x, y) + 1)
    #         res = max(res, best)
    #         return best
    #
    #     for i in range(m):
    #         for j in range(n):
    #             dfs(i, j)
    #     return res

    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #     memo = [[0] * n for _ in range(m)]
    #
    #     def dfs(i, j):
    #         if memo[i][j]:
    #             return memo[i][j]
    #
    #         memo[i][j] = 1
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 memo[i][j] = max(memo[i][j], dfs(x, y) + 1)
    #         return memo[i][j]
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             res = max(res, dfs(i, j))
    #     return res

    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #     memo = [[0] * n for _ in range(m)]
    #
    #     def dfs(i, j):
    #         if memo[i][j]:
    #             return memo[i][j]
    #         memo[i][j] = 1
    #
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 memo[i][j] = max(memo[i][j], dfs(x, y) + 1)
    #         return memo[i][j]
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             res = max(res, dfs(i, j))
    #     return res

    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #     memo = [[0] * n for _ in range(m)]
    #
    #     def dfs(i, j):
    #         if memo[i][j]:
    #             return memo[i][j]
    #
    #         memo[i][j] = 1
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 memo[i][j] = max(memo[i][j], dfs(x, y) + 1)
    #         return memo[i][j]
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             res = max(res, dfs(i, j))
    #     return res


    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #
    #     @lru_cache(None)
    #     def dfs(i, j):
    #         length = 1
    #
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 length = max(length, dfs(x, y) + 1)
    #
    #         return length
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             res = max(res, dfs(i, j))
    #
    #     return res

    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #
    #     @lru_cache(None)
    #     def dfs(i, j):
    #         best = 1
    #
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 best = max(best, dfs(x, y) + 1)
    #         return best
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             res = max(res, dfs(i, j))
    #     return res

    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #
    #     @lru_cache(None)
    #     def dfs(i, j):
    #         path = 1
    #
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 path = max(path, dfs(x, y) + 1)
    #
    #         return path
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             res = max(res, dfs(i, j))
    #     return res

    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #
    #     @lru_cache(None)
    #     def dfs(i, j):
    #         count = 1
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
    #                 count = max(count, 1 + dfs(x, y))
    #         return count
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             res = max(res, dfs(i, j))
    #     return res

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(i, j):
            count = 1

            for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    count = max(count, 1 + dfs(x, y))

            return count

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res


s = Solution()
nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
print(s.longestIncreasingPath(nums))

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
print(s.longestIncreasingPath(nums))

nums = [[1]]
print(s.longestIncreasingPath(nums))

nums = [[1,2]]
print(s.longestIncreasingPath(nums))


nums = [[6,8],[7,2]]
print(s.longestIncreasingPath(nums))

nums = [[7,7,5],[2,4,6],[8,2,0]]
print(s.longestIncreasingPath(nums))

