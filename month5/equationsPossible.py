# 等式方程的可满足性
from typing import List

# class UnionFind:
#     def __init__(self):
#         self.parent = list(range(26))
#
#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]
#
#     # 未使用按 rank 合并
#     def uoion(self, x, y):
#         self.parent[self.find(x)] = self.find(y)
#
#
# class Solution:
#     def equationsPossible(self, equations: List[str]) -> bool:
#         uf = UnionFind()
#         index = idx
#         for s in equations:
#             if s[1] == '=':
#                 index1 = ord(s[0]) - index
#                 index2 = ord(s[3]) - index
#                 uf.uoion(index1, index2)
#
#         for s in equations:
#             if s[1] == '!':
#                 index1 = ord(s[0]) - index
#                 index2 = ord(s[3]) - index
#                 if uf.find(index1) == uf.find(index2):
#                     return False
#
#         return True


# # 平时使用只用优化一个就行
# class UnionFind:
#     def __init__(self):
#         self.parent = list(range(26))  # 注意初始化条件
#
#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]
#
#     def union(self, x, y):
#         self.parent[self.find(x)] = self.find(y)
#
#
# class Solution:
#     def equationsPossible(self, equations: List[str]) -> bool:
#         uf = UnionFind()
#         index = ord('a')
#
#         for s in equations:
#             if s[1] == '=':
#                 uf.union(ord(s[0])-index, ord(s[3])-index)
#
#         for s in equations:
#             if s[1] == '!':
#                 if uf.find(ord(s[0])-index) == uf.find(ord(s[3])-index):
#                     return False
#         return True

# class UnionFind:
#     def __init__(self):
#         self.parent = list(range(26))
#
#     def find(self, i):
#         if i != self.parent[i]:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]
#
#     def union(self, x, y):
#         self.parent[self.find(x)] = self.find(y)
#
#
# class Solution:
#     def equationsPossible(self, equations: List[str]) -> bool:
#         uf = UnionFind()
#         idx = ord('a')
#
#         for s in equations:
#             if s[1] == '=':
#                 uf.union(ord(s[0]) - idx, ord(s[3]) - idx)
#
#         for s in equations:
#             if s[1] == '!':
#                 if uf.find(ord(s[0]) - idx) == uf.find(ord(s[3]) - idx):
#                     return False
#
#         return True

# class UnionFind:
#     def __init__(self):
#         self.parent = list(range(26))
#
#     def find(self, x):
#         if x != self.parent[x]:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#
#     def union(self, i, j):
#         x, y = self.find(i), self.find(j)
#         if x != y:
#             self.parent[x] = y
#
#
# class Solution:
#     def equationsPossible(self, equations: List[str]) -> bool:
#         uf = UnionFind()
#         i = ord('a')
#
#         for e in equations:
#             if e[1] == '=':
#                 uf.union(ord(e[0]) - i, ord(e[3]) - i)
#
#         for e in equations:
#             if e[1] == '!':
#                 if uf.find(ord(e[0]) - i) == uf.find(ord(e[3]) - i):
#                     return False
#         return True


class UnionFind:

    def __init__(self):
        self.parent = [i for i in range(26)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        self.parent[rootx] = rooty


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()

        a = ord('a')
        for e in equations:
            if e[1] == '=':
                uf.union(ord(e[0])-a, ord(e[3])-a)

        for e in equations:
            if e[1] == '!':
                if uf.find(ord(e[0])-a) == uf.find(ord(e[3])-a):
                    return False

        return True


s = Solution()
a = ["a==b","b!=a"]
print(s.equationsPossible(a))

a = ["b==a","a==b"]
print(s.equationsPossible(a))

a = ["a==b","b==c","a==c"]
print(s.equationsPossible(a))

a = ["a==b","b!=c","c==a"]
print(s.equationsPossible(a))

a = ["c==c","b==d","x!=z"]
print(s.equationsPossible(a))  # true
