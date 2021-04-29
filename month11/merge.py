# 56. 合并区间
from typing import List


class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     intervals.sort()
    #     res = [intervals[0]]
    #     for i in range(1, len(intervals)):
    #         if res[-1][1] >= intervals[i][0]:
    #             res[-1][1] = max(res[-1][1], intervals[i][1])
    #         else:
    #             res.append(intervals[i])
    #     return res

    # 看来还是考虑不融合的比较快
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     intervals.sort()
    #     res = []
    #     for interval in intervals:
    #         if not res or res[-1][1] < interval[0]:
    #             res.append(interval)
    #         else:
    #             res[-1][1] = max(res[-1][1], interval[1])
    #     return res

    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     intervals.sort(key=lambda x: x[1])
    #     res = []
    #     for a, b in intervals:
    #         while res and a <= res[-1][1]:
    #             a = min(a, res[-1][0])
    #             res.pop()
    #         res.append([a, b])
    #     return res

    # 按照第一个排序快
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for a, b in intervals:
            if not res or res[-1][1] < a:
                res.append([a, b])
            else:
                res[-1][1] = max(res[-1][1], b)
        return res


s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(intervals))

intervals = [[1,4],[4,5]]
print(s.merge(intervals))

intervals = [[1,4],[0,4]]
print(s.merge(intervals))

intervals = [[1,4],[2,3]]
print(s.merge(intervals))

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(s.merge(intervals))
