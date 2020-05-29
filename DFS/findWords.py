# 单词搜索
from typing import List


# 尚未解决：同一个单元格内的字母在一个单词中不允许被重复使用。
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         res = []
#
#         def DFS(word, row, col):
#             if not word:
#                 return True
#
#             char = word[0]
#             if row > 0 and board[row-1][col] == char:
#                 return DFS(word[1:], row-1, col)  # 莫要忘记 return
#             elif row < len(board)-1 and board[row+1][col] == char:
#                 return DFS(word[1:], row+1, col)
#             elif col > 0 and board[row][col-1] == char:
#                 return DFS(word[1:], row, col-1)
#             elif col < len(board[row])-1 and board[row][col+1] == char:
#                 return DFS(word[1:], row, col+1)
#             else:
#                 return False
#
#         for word in words:
#             skip = 0
#             for i in range(len(board)):
#                 for j in range(len(board[i])):
#                     if board[i][j] == word[0]:
#                         if DFS(word[1:], i, j):
#                             res.append(word)
#                             skip = 1
#                             break
#                 if skip:
#                     break
#
#         return res

class Solution:

    # # 使用 list
    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     # 预处理，构建字典树
    #     root = {}
    #     for word in words:
    #         node = root
    #         for char in word:
    #             node = node.setdefault(char, {})
    #         node['end'] = 1
    #
    #     res = []
    #     m, n = len(board), len(board[0])
    #
    #     def DFS(i, j, cur_word, cur_dict):
    #         cur_word += board[i][j]
    #         cur_dict = cur_dict[board[i][j]]
    #
    #         if 'end' in cur_dict and cur_dict['end'] == 1:
    #             res.append(cur_word)
    #             cur_dict['end'] = 0  # 防止重复数组加入 res，res 也可以使用 set
    #
    #         tmp, board[i][j] = board[i][j], '@'
    #         for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    #             x, y = i + dx, j + dy
    #             # board[x][y] != '@' 不用也可以，最后一个条件也会判定。当然最好用了。
    #             if 0 <= x < m and 0 <= y < n and board[x][y] != '@' and board[x][y] in cur_dict:
    #                 DFS(x, y, cur_word, cur_dict)
    #         board[i][j] = tmp
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] in root:
    #                 DFS(i, j, '', root)
    #
    #     return res

    # 使用 set
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = '#'

        res = set()
        m, n = len(board), len(board[0])

        def DFS(i, j, cur_word, cur_dict):
            cur_word += board[i][j]
            cur_dict = cur_dict[board[i][j]]

            if '#' in cur_dict:
                res.add(cur_word)

            tmp, board[i][j] = board[i][j], '@'
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] != '@' and board[x][y] in cur_dict:
                    DFS(x, y, cur_word, cur_dict)
            board[i][j] = tmp

        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    DFS(i, j, '', root)

        return list(res)


s = Solution()
words = ["a","b"]
board = [["a","b"]]
print(s.findWords(board, words))

words = ["oath","pea","eat","rain"]
board = [
          ['o','a','a','n'],
          ['e','t','a','e'],
          ['i','h','k','r'],
          ['i','f','l','v']
        ]
print(s.findWords(board, words))

words = ["a"]
board = [["a","a"]]
print(s.findWords(board, words))


words = ["aaa"]
board = [["a","a"]]
print(s.findWords(board, words))

words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
board = [["a","b"],["c","d"]]
print(s.findWords(board, words))
