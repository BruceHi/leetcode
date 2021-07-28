from typing import List
from math import ceil


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = 0
        if rungs[0] > dist:
            res = ceil(rungs[0]/dist) - 1
        for i in range(len(rungs)):
            if rungs[i] - rungs[i-1] > dist:
                res += ceil((rungs[i]-rungs[i-1]) / dist) - 1
        return res


s = Solution()
rungs = [1,3,5,10]
dist = 2
print(s.addRungs(rungs, dist))

rungs = [3,6,8,10]
dist = 3
print(s.addRungs(rungs, dist))

rungs = [3,4,6,7]
dist = 2
print(s.addRungs(rungs, dist))

rungs = [5]
dist = 10
print(s.addRungs(rungs, dist))

rungs = [3]
dist = 1
print(s.addRungs(rungs, dist))