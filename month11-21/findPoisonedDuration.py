# 495. 提莫攻击
from typing import List


class Solution:
    # def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    #     end = -1
    #     res = 0
    #     for t in timeSeries:
    #         if t > end:
    #             res += duration
    #         else:
    #             res += t + duration - 1 - end
    #         end = t + duration - 1
    #     return res

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        end = 0
        res = 0
        for t in timeSeries:
            if t >= end:
                res += duration
            else:
                res += t + duration - end
            end = t + duration
        return res



s = Solution()
timeSeries = [1,4]
duration = 2
print(s.findPoisonedDuration(timeSeries, duration))

timeSeries = [1,2]
duration = 2
print(s.findPoisonedDuration(timeSeries, duration))

timeSeries = [0,1]
duration = 2
print(s.findPoisonedDuration(timeSeries, duration))
