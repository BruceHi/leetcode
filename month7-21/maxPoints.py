from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0


s = Solution()
points = [[1,2,3],[1,5,1],[3,1,1]]
print(s.maxPoints(points))

points = [[1,5],[2,3],[4,2]]
print(s.maxPoints(points))

points = [[3, 4, 5], [4, 3, 3]]
print(s.maxPoints(points))
