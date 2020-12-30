# 47. 全排列 2
from typing import List
from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, set(permutations(nums))))


s = Solution()
nums = [1,1,2]
print(s.permuteUnique(nums))

nums = [1,2,3]
print(s.permuteUnique(nums))
