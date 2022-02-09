# 539. 最小时间差
from typing import List
from datetime import datetime


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def get_minute(a, b):
            return (datetime.strptime(b, '%H:%M') - datetime.strptime(a, '%H:%M')).seconds//60

        timePoints.sort()
        min_v = float('inf')
        sorted(timePoints)
        for i, t in enumerate(timePoints[:-1]):
            min_v = min(min_v, get_minute(t, timePoints[i+1]))
        min_v = min(min_v, get_minute(timePoints[-1], timePoints[0]))
        return min_v


s = Solution()
timePoints = ["23:59","00:00"]
print(s.findMinDifference(timePoints))

timePoints = ["00:00","23:59","00:00"]
print(s.findMinDifference(timePoints))

timePoints = ["01:01","02:01"]
print(s.findMinDifference(timePoints))
