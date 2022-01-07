# 2022. 将一维数组转变为二维数组
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        out = [[] for _ in range(m)]
        for i in range(m):
            out[i] = original[i*n:(i+1)*n]
        return out



s = Solution()
original = [1,2,3,4]
m = 2
n = 2
print(s.construct2DArray(original, m, n))

original = [1,2,3]
m = 1
n = 3
print(s.construct2DArray(original, m, n))

original = [1,2]
m = 1
n = 1
print(s.construct2DArray(original, m, n))

original = [3]
m = 1
n = 2
print(s.construct2DArray(original, m, n))

original = [1, 1, 1, 1]
m = 4
n = 1
print(s.construct2DArray(original, m, n))
