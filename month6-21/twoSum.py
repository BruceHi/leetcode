# 剑指 offer 57.和为 s 的两个数字
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while left < right:
            val = nums[left] + nums[right]
            if val == target:
                return [nums[left], nums[right]]
            elif val < target:
                left += 1
            else:
                right -= 1



s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))

nums = [10,26,30,31,47,60]
target = 40
print(s.twoSum(nums, target))
