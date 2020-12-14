# 289. 生命游戏
from typing import List
from itertools import product
from copy import deepcopy


class Solution:
    # def gameOfLife(self, board: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     m, n = len(board), len(board[0])
    #
    #     def alive(i, j):
    #         around = product([0, -1, 1], repeat=2)
    #         next(around)
    #         res = 0
    #         for dx, dy in around:
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and board[x][y]:
    #                 res += 1
    #         return res
    #
    #     nums = [[0] * n for _ in range(m)]
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] and alive(i, j) in [2, 3]:
    #                 nums[i][j] = 1
    #             if not board[i][j] and alive(i, j) == 3:
    #                 nums[i][j] = 1
    #     board[:] = nums

    # 若能将 board 扩充一圈，就不用那么多判断条件了
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        # 在外面多加一层 0
        board_copy = [[0] * (n+2)] + [[0] + row[:] + [0] for row in board] + [[0] * (n+2)]

        def alive(i, j):
            around = product([0, -1, 1], repeat=2)
            next(around)
            return [board_copy[i+dx][j+dy] for dx, dy in around].count(1)

        for i in range(1, m+1):
            for j in range(1, n+1):
                num = board_copy[i][j]
                if num and alive(i, j) not in (2, 3):
                    board[i-1][j-1] = 0
                elif not num and alive(i, j) == 3:
                    board[i-1][j-1] = 1


s = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
s.gameOfLife(board)
print(board)
