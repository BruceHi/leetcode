# 766. 托普利茨矩阵
from typing import List
from collections import deque

class Solution:
    # 超时,bfs
    # def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #     m, n = len(matrix), len(matrix[0])
    #     i, j = m-1, 0
    #     queue = deque([(i, j)])
    #     while queue:
    #         for _ in range(len(queue)):
    #             judge = set()
    #             i, j = queue.pop()
    #             for dx, dy in zip([-1, 0], [0, 1]):
    #                 x, y = i+dx, j+dy
    #                 if x >= 0 and y < n:
    #                     judge.add(matrix[x][y])
    #                     queue.append((x, y))
    #             if len(judge) > 1:
    #                 return False
    #     return True

    # def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #     m, n = len(matrix), len(matrix[0])
    #     for j in range(n):
    #         val = matrix[0][j]
    #         x, y = 0, j
    #         while x+1 < m and y+1 < n:
    #             x, y = x+1, y+1
    #             if matrix[x][y] != val:
    #                 return False
    #
    #     for i in range(1, m):
    #         val = matrix[i][0]
    #         x, y = i, 0
    #         while x+1 < m and y+1 < n:
    #             x, y = x+1, y+1
    #             if matrix[x][y] != val:
    #                 return False
    #
    #     return True

    # 对角线依次遍历
    # def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #     def judge(i, j):
    #         for x, y in zip(range(i+1, m), range(j+1, n)):
    #             if matrix[x][y] != matrix[i][j]:
    #                 return False
    #         return True
    #
    #     m, n = len(matrix), len(matrix[0])
    #     for j in range(n-1):
    #         if not judge(0, j):
    #             return False
    #
    #     for i in range(1, m-1):
    #         if not judge(i, 0):
    #             return False
    #
    #     return True

    # 是我想得太多了
    # def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #     m, n = len(matrix), len(matrix[0])
    #     for i in range(m-1):
    #         for j in range(n-1):
    #             if matrix[i+1][j+1] != matrix[i][j]:
    #                 return False
    #     return True

    # 直接取一行
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            if matrix[i][:-1] != matrix[i+1][1:]:
                return False
        return True


s = Solution()
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(s.isToeplitzMatrix(matrix))

matrix = [[1,2],[2,2]]
print(s.isToeplitzMatrix(matrix))
