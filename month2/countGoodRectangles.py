# 1725. 可以形成最大正方形的矩形数目
from typing import List
from collections import defaultdict


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = defaultdict(int)
        for a, b in rectangles:
            count[min(a, b)] += 1
        return count[max(count)]


s = Solution()
rectangles = [[5,8],[3,9],[5,12],[16,5]]
print(s.countGoodRectangles(rectangles))

rectangles = [[2,3],[3,7],[4,3],[3,7]]
print(s.countGoodRectangles(rectangles))

rectangles = [[5,8],[3,9],[3,12]]
print(s.countGoodRectangles(rectangles))
