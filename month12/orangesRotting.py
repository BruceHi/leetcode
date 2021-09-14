# 994.腐烂的橘子
# 广度优先遍历
from typing import List
from collections import deque


class Solution:
    # 每遍历一圈，time 加 1
    # def orangesRotting(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     queue = deque()
    #     count = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 count += 1
    #             elif grid[i][j] == 2:
    #                 queue.append((i, j))
    #     if not count:  # 初始都没有新鲜橘子了。
    #         return 0
    #
    #     time = -1
    #     while queue:
    #         time += 1
    #         for _ in range(len(queue)):
    #             i, j = queue.popleft()
    #             for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
    #                 x, y = i + dx, j + dy
    #                 if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
    #                     grid[x][y] = 2
    #                     queue.append((x, y))
    #
    #     for row in grid:
    #         if 1 in row:
    #             return -1
    #     return time

    # time 与 i，j 绑定在一起，写法更简单，不用额外判定初始就没有新鲜橘子的情况。
    # def orangesRotting(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     queue = deque()
    #     time = 0
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 2:
    #                 queue.append((i, j, time))
    #
    #     while queue:
    #         i, j, time = queue.popleft()
    #         for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
    #                 grid[x][y] = 2
    #                 queue.append((x, y, time+1))
    #
    #     for row in grid:
    #         if 1 in row:
    #             return -1
    #
    #     return time

    # def orangesRotting(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     queue = deque()
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 2:
    #                 queue.append((i, j))
    #
    #     res = 0
    #     while queue:
    #         res += 1
    #         for _ in range(len(queue)):
    #             i, j = queue.popleft()
    #             for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #                 x, y = i + dx, j + dy
    #                 if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
    #                     queue.append((x, y))
    #                     grid[x][y] = 2
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 return -1
    #
    #     return res-1 if res else 0

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))

        res = 0
        while queue:
            res += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        queue.append((x, y))
                        grid[x][y] = 2

        # 遍历完查看是否有新鲜橘子
        for row in grid:
            if 1 in row:
                return -1

        # res = 0 时，表示数组里面只有 0。表示 queue 为 空，即一开始就没有烂橘子，同时也没有好橘子，所以返回 0。
        return res-1 if res else 0


s = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(s.orangesRotting(grid))

grid = [[2,1,1],[0,1,1],[1,0,1]]
print(s.orangesRotting(grid))

grid = [[0,2]]
print(s.orangesRotting(grid))  # 返回 res-1

grid = [[0]]
print(s.orangesRotting(grid))  # 0， 0 分钟就没新鲜橘子了

grid = [[1]]
print(s.orangesRotting(grid)) # -1 永远不会腐烂
