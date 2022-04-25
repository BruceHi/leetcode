#
from typing import List


class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        res = 0
        for i, f in fruits:
            if f % limit == 0:
                res += time[i] * f // limit
            else:
                res += time[i] * (f // limit + 1)
        return res


s = Solution()
time = [2,3,2]
fruits = [[0,2],[1,4],[2,1]]
limit = 3
print(s.getMinimumTime(time, fruits, limit))

time = [1]
fruits = [[0,3],[0,5]]
limit = 2
print(s.getMinimumTime(time, fruits, limit))
