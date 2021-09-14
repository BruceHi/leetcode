from typing import List
from collections import Counter
from itertools import combinations
from math import factorial
import math


class Solution:
    # 超时
    # def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
    #     r = [a/b for a, b in rectangles]
    #     count = Counter(r)
    #     res = 0
    #     for k, v in count.items():
    #         if v >= 2:
    #             res += len(list(combinations(range(v), 2)))
    #     return res

    # 组合公式
    # def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
    #     r = [a/b for a, b in rectangles]
    #     count = Counter(r)
    #     res = 0
    #     for v in count.values():
    #         if v >= 2:
    #             res += factorial(v) // (factorial(2) * factorial(v-2))
    #     return res

    # 组合公式，可以化简
    # def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
    #     r = [a/b for a, b in rectangles]
    #     count = Counter(r)
    #     res = 0
    #     for v in count.values():
    #         if v >= 2:
    #             # res += v * (v-1) // 2
    #             # 3.8 的新功能
    #             res += math.comb(v, 2)
    #     return res


    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dic = {}
        res = 0
        for a, b in rectangles:
            v = a / b
            if v in dic:
                res += dic[v]
                dic[v] += 1
            else:
                dic[v] = 1
        return res


s = Solution()
rectangles = [[4,8],[3,6],[10,20],[15,30]]
print(s.interchangeableRectangles(rectangles))

rectangles = [[4,5],[7,8]]
print(s.interchangeableRectangles(rectangles))
