# 剑指 offer 53-1. 在排序数组中查找数字
from typing import List
import bisect


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     left = bisect.bisect_left(nums, target)
    #     if left == len(nums) or nums[left] != target:
    #         return 0
    #     right = bisect.bisect(nums, target)
    #     return right - left

    def search(self, nums: List[int], target: int) -> int:
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return 0
        right = bisect.bisect(nums, target)
        return right-left


s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.search(nums, target))

nums = [5,7,7,8,8,10]
target = 6
print(s.search(nums, target))
