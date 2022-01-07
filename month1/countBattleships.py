# 149. 甲板上的战舰
from typing import List


class Solution:
    # 解法一：岛屿数量
    # def countBattleships(self, board: List[List[str]]) -> int:
    #     m, n = len(board), len(board[0])
    #
    #     def dfs(i, j):
    #         board[i][j] = '.'
    #
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and board[x][y] == 'X':
    #                 dfs(x, y)
    #
    #     res = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == 'X':
    #                 res += 1
    #                 dfs(i, j)
    #     return res

    # 解法二：找固定的角，比如左上角、右上角、左下角、右下角等
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    res += 1
        return res




s = Solution()
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(s.countBattleships(board))

board = [["."]]
print(s.countBattleships(board))
