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
    #             cur_dict['end'] = 0  # 防止重复单词加入 res，res 也可以使用 set
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

    # # 使用 set
    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #
    #     root = {}
    #     for word in words:
    #         node = root
    #         for char in word:
    #             node = node.setdefault(char, {})
    #         node['#'] = '#'
    #
    #     res = set()
    #     m, n = len(board), len(board[0])
    #
    #     def DFS(i, j, cur_word, cur_dict):
    #         cur_word += board[i][j]
    #         cur_dict = cur_dict[board[i][j]]
    #
    #         if '#' in cur_dict:
    #             res.add(cur_word)
    #
    #         tmp, board[i][j] = board[i][j], '@'
    #         for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and board[x][y] != '@' and board[x][y] in cur_dict:
    #                 DFS(x, y, cur_word, cur_dict)
    #         board[i][j] = tmp
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] in root:
    #                 DFS(i, j, '', root)
    #
    #     return list(res)

    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     res = []
    #     m, n = len(board), len(board[0])
    #
    #     root = {}
    #     for word in words:
    #         cur = root
    #         for c in word:
    #             cur = cur.setdefault(c, {})
    #         cur['end'] = 1
    #
    #     def dfs(i, j, cur_word, cur_dic):
    #         cur_word += board[i][j]
    #         cur_dic = cur_dic[board[i][j]]
    #
    #         if cur_dic.get('end', 0):
    #             res.append(cur_word)
    #             cur_dic['end'] = 0
    #
    #         tmp, board[i][j] = board[i][j], '@'
    #         for idx, idy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + idx, j + idy
    #             if 0 <= x < m and 0 <= y < n and board[x][y] in cur_dic:
    #                 dfs(x, y, cur_word, cur_dic)
    #         board[i][j] = tmp
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] in root:
    #                 dfs(i, j, '', root)
    #
    #     return res

    # 超时
    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     m, n = len(board), len(board[0])
    #
    #     def ExistWord(word):
    #         def dfs(i, j, cur):
    #             if not cur:
    #                 return True
    #
    #             tmp = board[i][j]
    #             board[i][j] = ''
    #             res = False
    #
    #             for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #                 x, y = i + dx, j + dy
    #                 if 0 <= x < m and 0 <= y < n and cur[0] == board[x][y]:
    #                     if dfs(x, y, cur[1:]):
    #                         res = True
    #                         break
    #             board[i][j] = tmp
    #             return res
    #
    #         for i in range(m):
    #             for j in range(n):
    #                 if word[0] == board[i][j]:
    #                     if dfs(i, j, word[1:]):
    #                         return True
    #         return False
    #
    #     return [word for word in words if ExistWord(word)]

    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     root = {}
    #     for word in words:
    #         node = root
    #         for c in word:
    #             node = node.setdefault(c, {})
    #         node['#'] = '#'
    #
    #     m, n = len(board), len(board[0])
    #     res = set()
    #
    #     def dfs(i, j, cur, dic):
    #         if '#' in dic:
    #             res.add(cur)
    #             # return  # 不能return，可能会出现 ['oaa', 'oa'] 这种情况。
    #
    #         tmp = board[i][j]
    #         board[i][j] = ''
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and board[x][y] in dic:
    #                 dfs(x, y, cur+board[x][y], dic[board[x][y]])
    #         board[i][j] = tmp
    #
    #     for i in range(m):
    #         for j in range(n):
    #             v = board[i][j]
    #             if v in root:
    #                 dfs(i, j, v, root[v])
    #     return list(res)

    # 注意与上面的略微不同，主要 是 dfs 中 cur 和 dic 的写法不同，是在定义前还是定义后赋值
    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     root = {}
    #     for word in words:
    #         node = root
    #         for c in word:
    #             node = node.setdefault(c, {})
    #         node['#'] = '#'
    #
    #     m, n = len(board), len(board[0])
    #     res = set()
    #
    #     def dfs(i, j, cur, dic):
    #         v = board[i][j]
    #         cur += v
    #         dic = dic[v]
    #
    #         if '#' in dic:
    #             res.add(cur)
    #             # return  # 不能return，可能会出现 ['oaa', 'oa'] 这种情况。
    #
    #         board[i][j] = ''
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and board[x][y] in dic:
    #                 dfs(x, y, cur, dic)
    #         board[i][j] = v
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] in root:
    #                 dfs(i, j, '', root)
    #     return list(res)


    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     root = {}
    #     for word in words:
    #         node = root
    #         for c in word:
    #             node = node.setdefault(c, {})
    #         node['#'] = '#'
    #
    #     m, n = len(board), len(board[0])
    #     res = set()
    #
    #     def dfs(i, j, cur, dic):
    #         v = board[i][j]
    #         cur += v
    #         dic = dic[v]
    #
    #         if '#' in dic:
    #             res.add(cur)
    #             # return  # 不能return，可能会出现 ['oaa', 'oa'] 这种情况。
    #
    #         board[i][j] = ''
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and board[x][y] in dic:
    #                 dfs(x, y, cur, dic)
    #         board[i][j] = v
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] in root:
    #                 dfs(i, j, '', root)
    #     return list(res)


    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     root = {}
    #     for word in words:
    #         node = root
    #         for c in word:
    #             node = node.setdefault(c, {})
    #         node['#'] = '#'
    #
    #     m, n = len(board), len(board[0])
    #     res = set()
    #
    #     def dfs(i, j, cur, dic):
    #         v = board[i][j]
    #         cur += v
    #         dic = dic[v]
    #
    #         if '#' in dic:
    #             res.add(cur)
    #
    #         board[i][j] = ''
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and board[x][y] in dic:
    #                 dfs(x, y, cur, dic)
    #         board[i][j] = v
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] in root:
    #                 dfs(i, j, '', root)
    #
    #     return list(res)


    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     root = {}
    #     for word in words:
    #         node = root
    #         for c in word:
    #             node = node.setdefault(c, {})
    #         node['#'] = '#'
    #
    #     m, n = len(board), len(board[0])
    #     res = set()
    #
    #     def dfs(i, j, cur, dic):
    #         v = board[i][j]
    #         cur += v
    #         dic = dic[v]
    #
    #         if '#' in dic:
    #             res.add(cur)
    #
    #         board[i][j] = ''
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and board[x][y] in dic:
    #                 dfs(x, y, cur, dic)
    #         board[i][j] = v
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] in root:
    #                 dfs(i, j, '', root)
    #     return list(res)

    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     root = {}
    #     for word in words:
    #         node = root
    #         for c in word:
    #             node = node.setdefault(c, {})
    #         node['#'] = '#'
    #
    #     res = set()
    #     m, n = len(board), len(board[0])
    #     def dfs(i, j, cur, root):
    #         v = board[i][j]
    #         cur += v
    #         node = root[v]
    #
    #         if '#' in node:
    #             res.add(cur)
    #
    #         board[i][j] = ''
    #         for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
    #             x, y = i + dx, j + dy
    #             if 0 <= x < m and 0 <= y < n and board[x][y] in node:
    #                 dfs(x, y, cur, node)
    #         board[i][j] = v
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] in root:
    #                 dfs(i, j, '', root)
    #     return list(res)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = '#'

        res = set()
        m, n = len(board), len(board[0])

        def dfs(i, j, cur, root):
            v = board[i][j]
            cur += v
            node = root[v]

            if '#' in node:
                res.add(cur)

            board[i][j] = '.'
            for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] in node:
                    dfs(x, y, cur, node)
            board[i][j] = v

        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i, j, '', root)
        return list(res)


s = Solution()
words = ["a", "b"]
board = [["a", "b"]]
print(s.findWords(board, words))

words = ["oath", "pea", "eat", "rain"]
board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
print(s.findWords(board, words))

words = ["a"]
board = [["a", "a"]]
print(s.findWords(board, words))

words = ["aaa"]
board = [["a", "a"]]
print(s.findWords(board, words))

words = ["ab", "cb", "ad", "bd", "ac", "ca", "da", "bc", "db", "adcb", "dabc", "abb", "acb"]
board = [["a", "b"], ["c", "d"]]
print(s.findWords(board, words))


board = [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
words = ["oa", "oaa"]
print(s.findWords(board, words))  # ["oa","oaa"]
