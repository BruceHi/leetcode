# 朋友圈
from typing import List


# class Solution:

    # # 邻接矩阵的深度优先遍历 看不懂
    # def findCircleNum(self, M: List[List[int]]) -> int:
    #     n = len(M)
    #     visited = [0] * n
    #
    #     # 按照诸如 [1, 2], [2, 3], [3, 5] 等可以标记 1， 2， 3，5 索引处为 1.
    #     def DFS(i):
    #         for j in range(n):
    #             if M[i][j] and not visited[j]:
    #                 visited[j] = 1
    #                 DFS(j)
    #
    #     count = 0
    #     for i in range(n):
    #         if not visited[i]:
    #             DFS(i)
    #             count += 1
    #
    #     return count

    # # 并查集简化版本
    # def findCircleNum(self, M: List[List[int]]) -> int:
    #     n = len(M)
    #     count = n
    #     p = {i: {i} for i in range(n)}
    #
    #     p = set()
    #     for i in range(n-1):
    #         for j in range(i, n):
    #             if M[i][j] and i :


# 并查集
# class UnionFind:
#     def __init__(self, M):
#         n = len(M)
#         self.rank = [1] * n
#         self.parent = [i for i in range(n)]
#         self.count = n
#
#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]
#
#     def union(self, x, y):
#         rootx = self.find(x)
#         rooty = self.find(y)
#         if rootx != rooty:
#             if self.rank[rootx] < self.rank[rooty]:
#                 self.parent[rootx] = rooty
#             else:
#                 self.parent[rooty] = rootx
#                 if self.rank[rootx] == self.rank[rooty]:
#                     self.rank[rootx] += 1
#             self.count -= 1
#
#
# class Solution:
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         uf = UnionFind(M)
#         n = len(M)
#
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if M[i][j]:
#                     uf.union(i, j)
#
#         return uf.count

class Solution:
    # 邻接矩阵的 dfs
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [0] * n

        def dfs(i):
            for j in range(n):
                if M[i][j] and not visited[j]:
                    visited[j] = 1
                    dfs(j)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count

# class UnionFind:
#     def __init__(self, M):
#         n = len(M)
#         self.parent = [_ for _ in range(n)]
#         self.count = n
#
#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]
#
#     def unoion(self, x, y):
#         rootx = self.find(x)
#         rooty = self.find(y)
#         if rootx != rooty:
#             self.parent[rootx] = self.find(rooty)
#             self.count -= 1
#
#
# class Solution:
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         uf = UnionFind(M)
#         n = len(M)
#
#         for i in range(1, n):
#             for j in range(i):
#                 if M[i][j]:
#                     uf.unoion(i, j)
#         return uf.count


s = Solution()
m = [[1,1,0],
     [1,1,0],
     [0,0,1]]
print(s.findCircleNum(m))

m = [[1,0,0,1],
     [0,1,1,0],
     [0,1,1,1],
     [1,0,1,1]]
print(s.findCircleNum(m))


m = [[1,1,0],
     [1,1,1],
     [0,1,1]]
print(s.findCircleNum(m))


m = [[1,1,1],[1,1,1],[1,1,1]]
print(s.findCircleNum(m))
