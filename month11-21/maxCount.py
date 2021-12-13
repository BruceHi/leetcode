# 598. 范围求和
from typing import List


class Solution:
    # def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    #     if not ops:
    #         return m * n
    #     r = [float('inf'), float('inf')]
    #     for a, b in ops:
    #         if a < r[0]:
    #             r[0] = a
    #         if b < r[1]:
    #             r[1] = b
    #     return r[0] * r[1]

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_a, min_b = m, n
        for a, b in ops:
            min_a = min(min_a, a)
            min_b = min(min_b, b)
        return min_a * min_b


s = Solution()
m = 3
n = 3
operations = [[2,2],[3,3]]
print(s.maxCount(m, n, operations))
