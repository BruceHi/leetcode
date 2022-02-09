# 1748. 唯一元素的和
from typing import List
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sum(k for k, v in count.items() if v == 1)


s = Solution()
nums = [1,2,3,2]
print(s.sumOfUnique(nums))

nums = [1,1,1,1,1]
print(s.sumOfUnique(nums))

nums = [1,2,3,4,5]
print(s.sumOfUnique(nums))
