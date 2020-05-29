# 解数独（只需一个解即可）
from typing import List


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)

    def solve(self, board):

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for nums in range(1, 10):
                        if self.is_valid(board, i, j, str(nums)):
                            board[i][j] = str(nums)
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'  # 失败则回过去。
                    return False
        return True

    def is_valid(self, board, row, col, c):
        for i in range(9):
            if board[row][i] == c:  # 行
                return False
            if board[i][col] == c:  # 列
                return False

            box_index = (row//3)*3 + col//3  # 块
            for j in range(9):
                if (i//3)*3 + j//3 == box_index:
                    if board[i][j] == c:
                        return False
        return True


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
print(board1)
