# 解数独（只需一个解即可）
from typing import List
import string
from Array.isValidSudoku import isValidSudoku


class Solution:

    # def solveSudoku(self, board: List[List[str]]) -> None:
    #     self.solve(board)
    #
    # def solve(self, board):
    #
    #     for i in range(9):
    #         for j in range(9):
    #             if board[i][j] == '.':
    #                 for nums in range(1, 10):
    #                     if self.is_valid(board, i, j, str(nums)):
    #                         board[i][j] = str(nums)
    #                         if self.solve(board):
    #                             return True
    #                         else:
    #                             board[i][j] = '.'  # 失败则回过去。
    #                 return False
    #     return True
    #
    # def is_valid(self, board, row, col, c):
    #     for i in range(9):
    #         if board[row][i] == c:  # 行
    #             return False
    #         if board[i][col] == c:  # 列
    #             return False
    #
    #         box_index = (row//3)*3 + col//3  # 块
    #         for j in range(9):
    #             if (i//3)*3 + j//3 == box_index:
    #                 if board[i][j] == c:
    #                     return False
    #     return True

    # def solveSudoku(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     def valid(i, j, num):
    #         if num in board[i]:
    #             return False
    #
    #         for x in range(9):
    #             if num == board[x][j]:
    #                 return False
    #
    #             idx = i // 3 * 3 + j // 3
    #             for y in range(9):
    #                 if x//3*3 + y//3 == idx:
    #                     if num == board[x][y]:
    #                         return False
    #         return True
    #
    #
    #     def dfs(board):
    #         for i in range(9):
    #             for j in range(9):
    #                 if board[i][j] == '.':
    #                     for num in string.digits[1:]:
    #                         if valid(i, j, num):
    #                             board[i][j] = num
    #                             if dfs(board):
    #                                 return True
    #                             else:
    #                                 board[i][j] = '.'
    #                     return False  # 若是 1-9 都无法满足，返回 False，下面写也可以
    #                     # else:
    #                     #     return False
    #
    #         return True  # 最后发现没有可遍历的了，返回 True
    #
    #     dfs(board)

    def solveSudoku(self, board: List[List[str]]) -> None:

        def is_valid(board, i, j, c):
            if c in board[i]:
                return False

            idx = i // 3 * 3 + j // 3
            for x in range(9):
                if c == board[x][j]:
                    return False

                for y in range(9):
                    if x//3*3 + y//3 == idx:
                        if c == board[x][y]:
                            return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in string.digits[1:]:
                            if is_valid(board, i, j, c):
                                board[i][j] = c
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True

        solve(board)


s = Solution()
board1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
s.solveSudoku(board1)
# board1[8][8] = '8'
print(isValidSudoku(board1))
print(board1)
