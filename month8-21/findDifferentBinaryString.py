from typing import List
from itertools import product


class Solution:
    def findDifferentBinaryString(self, nums: List[str]):
        for x in [''.join(x) for x in product('10', repeat=len(nums[0]))]:
            if x not in set(nums):
                return x

s = Solution()
nums = ["01","10"]
print(s.findDifferentBinaryString(nums))

nums = ["00","01"]
print(s.findDifferentBinaryString(nums))

nums = ["111","011","001"]
print(s.findDifferentBinaryString(nums))
