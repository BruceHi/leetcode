# 有效的数独
from typing import List

# def isValidSudoku(board):
#     for i in range(9):
#         if not isOnlyNumber(board[i]):
#             return False
#
#     for j in range(9):
#         temp = [board[i][j] for i in range(9)]
#         if not isOnlyNumber(temp):
#             return False
#
#     temp1 = []
#     for m in (0, 3, 6):  # 控制外层循环
#         for n in (0, 3, 6):  # 控制内存循环
#             for i in range(m, m + 3):
#                 temp = [board[i][j] for j in range(n, n + 3)]
#                 temp1.extend(temp)
#             if not isOnlyNumber(temp1):
#                 return False
#             temp1 = []
#
#     return True


# def isValidSudoku(board):
#     rows = [set() for _ in range(9)]
#     columns = [set() for _ in range(9)]
#     boxes = [set() for _ in range(9)]
#     for i in range(9):
#         for j in range(9):
#             val = board[i][j]
#             if val != '.':
#                 box_index = (i//3)*3 + j//3
#                 if val in rows[i] or val in columns[j] or val in boxes[box_index]:
#                     return False
#                 rows[i].add(val)
#                 columns[j].add(val)
#                 boxes[box_index].add(val)
#     return True

def isValidSudoku(board: List[List[str]]) -> bool:
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    box = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            tmp = board[i][j]
            if tmp != '.':
                index = i//3*3 + j//3
                if tmp in row[i] or tmp in col[j] or tmp in box[index]:
                    return False
                row[i].add(tmp)
                col[j].add(tmp)
                box[index].add(tmp)
    return True




board1 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
#
# temp1 = []

# for i in range(3):
#     temp = [board1[i][j] for j in range(3)]
#     temp1.extend(temp)
# print(temp1)


# for k in (0, 3, 6):
#     for i in range(3):
#         temp = [board1[i][j] for j in range(k, k + 3)]
#         temp1.extend(temp)
#     print(temp1)
#     temp1 = []

# for m in (0, 3, 6):
#     for k in (0, 3, 6):
#         for i in range(m, m + 3):
#             temp = [board1[i][j] for j in range(k, k + 3)]
#             temp1.extend(temp)
#         print(temp1)
#         temp1 = []
#
# print(set(temp1))
print(isValidSudoku(board1))

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
# from collections import Iterable
#
# print(isinstance(board1, Iterable))
# print(set(board1))
#
# list3 = [1, 2, 6, '5']
# print(set(list3))
# print(type(board1))
print(isValidSudoku(board1))


# list1 = ["5","3",".",".","7",".",".",".","."]
# print(isOnlyNumber(list1))
#
# list1 = [".", "8", "8", ".", ".", ".", ".", "6", "."]
# print(isOnlyNumber(list1))

