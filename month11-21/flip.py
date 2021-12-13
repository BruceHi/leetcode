# 519. 随机翻转矩阵
from typing import List
from random import randint


# 超时
# class Solution:
#
#     def __init__(self, m: int, n: int):
#         self.m = m
#         self.n = n
#         self.matrix = [[0] * n for _ in range(m)]
#
#     def flip(self) -> List[int]:
#         res = []
#         for i in range(self.m):
#             for j in range(self.n):
#                 if self.matrix[i][j] == 0:
#                     res.append((i, j))
#         a, b = choice(res)
#         self.matrix[a][b] = 1
#         return [a, b]
#
#     def reset(self) -> None:
#         self.matrix = [[0] * self.n for _ in range(self.m)]

# # 还是超时
# class Solution:
#
#     def __init__(self, m: int, n: int):
#         self.m = m
#         self.n = n
#         self.record = set((i, j) for i in range(m) for j in range(n))
#         self.matrix = [[0] * n for _ in range(m)]
#
#     def flip(self) -> List[int]:
#         a, b = choice(list(self.record))
#         self.record.remove((a, b))
#         self.matrix[a][b] = 1
#         return [a, b]
#
#     def reset(self) -> None:
#         self.matrix = [[0] * self.n for _ in range(self.m)]
#         self.record = [(i, j) for i in range(self.m) for j in range(self.n)]
class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.record = {}

    # 注意 total 的大小
    def flip(self) -> List[int]:
        r = randint(0, self.total-1)
        i = self.record.get(r, r)

        self.total -= 1
        self.record[r] = self.record.get(self.total, self.total)
        return [i//self.n, i%self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.record.clear()


# s = Solution(3, 1)
# print(s.flip())
# print(s.flip())
# print(s.flip())
# s.reset()
# print(s.flip())

s = Solution(2, 2)
print(s.flip())
print(s.flip())
print(s.flip())
print(s.flip())
