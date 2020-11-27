# 581. 最短无序连续子数组
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        nums_sort = sorted(nums)
        left = 0
        right = n - 1
        while left <= right and nums[left] == nums_sort[left]:
            left += 1
        while left <= right and nums[right] == nums_sort[right]:
            right -= 1
        return right-left+1


s = Solution()
nums = [2, 6, 4, 8, 10, 9, 15]
print(s.findUnsortedSubarray(nums))

nums = [1, 2, 3, 4]
print(s.findUnsortedSubarray(nums))

nums = [2, 6, 4, 8, 10, 9, 15, 11, 16]
print(s.findUnsortedSubarray(nums))

nums = [2, 6, 4, 8, 10, 9, 15, 1, 2]
print(s.findUnsortedSubarray(nums))

nums = [1, 4, 7, 2, 9]
print(s.findUnsortedSubarray(nums))

nums = [1, 4, 7, 2, 5]
print(s.findUnsortedSubarray(nums))

nums = [3,2,3,2,4]
print(s.findUnsortedSubarray(nums))

nums = [1, 3, 5, 4, 2]
print(s.findUnsortedSubarray(nums))

nums = [1, 3, 2, 5, 4]
print(s.findUnsortedSubarray(nums))