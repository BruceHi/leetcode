# 79. 单词搜索
from typing import List


class Solution:

    # # 成功，比较慢
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #
    #     m, n = len(board), len(board[0])
    #
    #     def dfs(i, j, word, cur):
    #         if not word:
    #             return True
    #
    #         for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and board[x][y] == word[0] and [x, y] not in cur:
    #                 if dfs(x, y, word[1:], cur + [[x, y]]):
    #                     return True
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == word[0]:
    #                 if dfs(i, j, word[1:], [[i, j]]):
    #                     return True
    #     return False

    # # 换成集合，超时，使用 any 遍历完所有结果
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #
    #     m, n = len(board), len(board[0])
    #
    #     def dfs(i, j, word, cur):
    #         if not word:
    #             return True
    #
    #         res = []
    #         for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and board[x][y] == word[0] and (x, y) not in cur:
    #                 cur.add((x, y))
    #                 res.append(dfs(x, y, word[1:], cur))
    #                 cur.remove((x, y))
    #         return any(res)  # 有一个 True，返回 True，这样比较慢
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == word[0]:
    #                 if dfs(i, j, word[1:], {(i, j)}):
    #                     return True
    #     return False

    # 更改是否访问过的方式，使用染色，通过
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        def dfs(i, j, word, board):
            if not word:
                return True

            result = False
            tmp = board[i][j]
            board[i][j] = None
            for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == word[0]:
                    if dfs(x, y, word[1:], board):
                        result = True
                        break  # 直接中断循环，比较快
            board[i][j] = tmp
            return result

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:], board):
                        return True
        return False


s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(s.exist(board, "ABCCED"))

print(s.exist(board, "SEE"))

print(s.exist(board, "ABCB"))
