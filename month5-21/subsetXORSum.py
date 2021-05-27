from typing import List
from itertools import combinations
from functools import reduce


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(nums):
            if len(nums) == 1:
                return nums[0]
            return reduce(lambda x, y: x ^ y, nums)
        res = 0
        for i in range(1, len(nums)+1):
            for a in combinations(nums, i):
                res += xor(a)
        return res


s = Solution()
nums = [1,3]
print(s.subsetXORSum(nums))

nums = [5,1,6]
print(s.subsetXORSum(nums))

nums = [3,4,5,6,7,8]
print(s.subsetXORSum(nums))
