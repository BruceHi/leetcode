class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        pass
        # grid = [[0] * n for _ in range(m)]
        # res = 0
        #
        # def dfs(i, j):
        #     if i == m - 1 and j == n - 1:
        #         nonlocal res
        #         res += 1
        #     for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        #         x, y = i + dx, j + dy
        #         if 0 < x < m and 0 < y < n:
        #
        #             for da, db in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        #                 a, b = x + da, y + db
        #                 if 0 < a < m and 0 < a < n:
        #
        #                     if
        # dfs


s = Solution()
m = 1
n = 1
print(s.colorTheGrid(m, n))

m = 1
n = 2
print(s.colorTheGrid(m, n))

m = 5
n = 5
print(s.colorTheGrid(m, n))
