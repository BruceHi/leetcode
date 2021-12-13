# 1337. 矩阵中
from typing import List
from collections import defaultdict


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        dic = {}
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dic[i] = j
                    break
            if i not in dic:
                dic[i] = n
        idx = sorted(dic, key=lambda x: dic[x])
        return idx[:k]




s = Solution()
mat = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]
k = 3
print(s.kWeakestRows(mat, k))

mat = [[1, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]
k = 2
print(s.kWeakestRows(mat, k))
