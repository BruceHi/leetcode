# 有序矩阵中第K小的元素
from typing import List
import heapq

class Solution:
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     res = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))]
    #     return heapq.nsmallest(k, res)[k-1]

    # 时间复杂度 O(n^2 log n)
    # def kthSmallest(self, matrix: List[List[int]], k: int):
    #     return sorted(sum(matrix, []))[k-1]

    # 堆，时间复杂度 O(k log n)
    def kthSmallest(self, matrix: List[List[int]], k: int):
        n = len(matrix)
        queue = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(queue)

        for _ in range(k-1):  # 运行次数，弹出 k-1 个小的值。
            _, x, y = heapq.heappop(queue)
            if y != n-1:
                heapq.heappush(queue, (matrix[x][y+1], x, y+1))
        return queue[0][0]


s = Solution()
matrix = [
   [1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(s.kthSmallest(matrix, k))

