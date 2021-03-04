# 57. 插入区间
from typing import List


class Solution:
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     if not intervals:
    #         return [newInterval]
    #     a, b = newInterval
    #     res = []
    #     n = len(intervals)
    #
    #     # 直接插入两边
    #     if b < intervals[0][0]:
    #         res = [newInterval] + intervals
    #         return res
    #
    #     if a > intervals[-1][1]:
    #         res = intervals + [newInterval]
    #         return res
    #
    #     flag = False  # 插入
    #     idx = 0
    #     for i, inter in enumerate(intervals):
    #         if set(range(inter[0], inter[1]+1)) & set(range(a, b+1)):
    #             flag = True
    #             idx = i
    #             res.append([min(inter[0], a), max(inter[1], b)])
    #             break
    #         res.append(inter)
    #
    #     # 直接插入
    #     if not flag:
    #         i = 0
    #         while i < n-1:
    #             if res[i][1] < a and b < res[i+1][0]:
    #                 res.insert(i+1, newInterval)
    #                 return res
    #             i += 1
    #
    #     i = idx + 1
    #     while i < n:
    #         if res[-1][1] >= intervals[i][0]:
    #             res[-1][1] = max(res[-1][1], intervals[i][1])
    #             i += 1
    #         else:
    #             res.extend(intervals[i:])
    #             break
    #
    #     return res

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []
        for inter in intervals:
            if not res or res[-1][1] < inter[0]:
                res.append(inter)
            else:
                res[-1][1] = max(res[-1][1], inter[1])
        return res


s = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(s.insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(s.insert(intervals, newInterval))

intervals = []
newInterval = [5,7]
print(s.insert(intervals, newInterval))

intervals = [[1,5]]
newInterval = [2,3]
print(s.insert(intervals, newInterval))

intervals = [[1,5]]
newInterval = [2,7]
print(s.insert(intervals, newInterval))

intervals = [[1,5]]
newInterval = [0,3]
print(s.insert(intervals, newInterval))

intervals = [[1,5]]
newInterval = [0,6]
print(s.insert(intervals, newInterval))

# 没有融合
intervals = [[1, 5]]
newInterval = [6, 8]
print(s.insert(intervals, newInterval))

intervals = [[1, 2], [4, 6], [9, 10]]
newInterval = [7, 8]
print(s.insert(intervals, newInterval))

intervals = [[0,10],[14,14],[15,20]]
newInterval = [11, 11]
print(s.insert(intervals, newInterval))

intervals = [[3,5],[12,15]]
newInterval = [6, 6]
print(s.insert(intervals, newInterval))
