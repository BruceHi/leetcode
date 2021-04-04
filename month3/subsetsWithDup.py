# 90.子集 2
from typing import List
from itertools import combinations, permutations


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            tmp = set(map(lambda x: tuple(sorted(x)), combinations(nums, i)))
            # print(tmp)
            res.extend(list(map(list, tmp)))
        return res


s = Solution()
nums = [1, 2, 2]
print(s.subsetsWithDup(nums))

nums = [0]
print(s.subsetsWithDup(nums))

nums = [4,4,4,1,4]
print(s.subsetsWithDup(nums))
