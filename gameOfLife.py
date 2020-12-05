# 289. 生命游戏
from typing import List
from itertools import product


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
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def alive(i, j):
            around = product([0, -1, 1], repeat=2)
            next(around)
            res = 0
            for dx, dy in around:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y]:
                    res += 1
            return res

        nums = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] and alive(i, j) in [2, 3]:
                    nums[i][j] = 1
                if not board[i][j] and alive(i, j) == 3:
                    nums[i][j] = 1
        board[:] = nums




s = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
s.gameOfLife(board)
print(board)
