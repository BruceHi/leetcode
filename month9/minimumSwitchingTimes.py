from typing import List
from collections import Counter


class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        def flap(nums):
            res = []
            for num in nums:
                res.extend(num)
            return res

        source = flap(source)
        target = flap(target)
        count1 = Counter(source)
        count2 = Counter(target)
        return len(list((count1 - count2).elements()))


s = Solution()
source = [[1,3],[5,4]]
target = [[3,1],[6,5]]
print(s.minimumSwitchingTimes(source, target))

source = [[1,2,3],[3,4,5]]
target = [[1,3,5],[2,3,4]]
print(s.minimumSwitchingTimes(source, target))
