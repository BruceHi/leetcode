# 794. 有效的井字游戏
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        pass


s = Solution()
board = ["O  ","   ","   "]
print(s.validTicTacToe(board))

board = ["XOX"," X ","   "]
print(s.validTicTacToe(board))

board = ["XXX","   ","OOO"]
print(s.validTicTacToe(board))

board = ["XOX","O O","XOX"]
print(s.validTicTacToe(board))
