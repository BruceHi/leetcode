# 130. 被围绕的区域
from typing import List
from functools import lru_cache


class Solution:

    # def solve(self, board: List[List[str]]) -> None:
    #     if not board:
    #         return
    #     m, n = len(board), len(board[0])
    #     if m <= 2 or n <= 2:
    #         return
    #     for i in range(1, m-1):
    #         for j in range(1, n-1):
    #             if [board[i-1][j], board[i+1][j], board[i][j-1], board[i][j+1]].count('X') >= 3:
    #                 board[i][j] = 'X'

    # def solve(self, board: List[List[str]]) -> None:
    #     if not board:
    #         return
    #     m, n = len(board), len(board[0])
    #     if m <= 2 or n <= 2:
    #         return
    #     for i in range(1, m-1):
    #         for j in range(1, n-1):
    #             if [board[i-1][j], board[i+1][j], board[i][j-1], board[i][j+1]].count('X') >= 3:
    #                 board[i][j] = 'X'

    # 不被包围的 O 都直接或间接与边界上的 O 相连。这点很重要。
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])

        # 没有提高多少
        @lru_cache(None)
        def dfs(i, j):
            board[i][j] = 'A'
            for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    dfs(x, y)

        # 1 列和最后一列
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)

        # 1 行和最后一行
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m-1][j] == 'O':
                dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'





s = Solution()
board = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X']]
s.solve(board)
print(board)

board = []
s.solve(board)
print(board)

board = [["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]]
s.solve(board)
print(board)
