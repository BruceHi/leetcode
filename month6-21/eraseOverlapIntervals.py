# 435. 无重叠区间
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = 0
        j = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[j][1]:
                res += 1
            else:
                j = i
        return res


s = Solution()
intervals = [[1,2], [2,3], [3,4], [1,3]]
print(s.eraseOverlapIntervals(intervals))

intervals = [[1,2], [1,2], [1,2]]
print(s.eraseOverlapIntervals(intervals))

intervals = [[1,2], [2,3]]
print(s.eraseOverlapIntervals(intervals))

intervals = [[1,2]]
print(s.eraseOverlapIntervals(intervals))

intervals = [[1,100],[11,22],[1,11],[2,12]]
print(s.eraseOverlapIntervals(intervals))  # 2

intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
print(s.eraseOverlapIntervals(intervals))  # 2
