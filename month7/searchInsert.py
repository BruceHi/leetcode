# 搜索插入位置
from typing import List
import bisect


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


s = Solution()
print(s.searchInsert([1,3,5,6], 5))

print(s.searchInsert([1,3,5,6], 2))

print(s.searchInsert([1,3,5,6], 7))

print(s.searchInsert([1,3,5,6], 0))
