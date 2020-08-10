# 寻找旋转排序数组中的最小值（有重复）
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[right]



s = Solution()
nums = [3,4,5,1,2]
print(s.findMin(nums))


nums = [4,5,6,7,0,1,2]
print(s.findMin(nums))


nums = [1, 2, 3]
print(s.findMin(nums))


nums = [2, 3, 4, 5, 1]
print(s.findMin(nums))

nums = [2,2,2,0,1]
print(s.findMin(nums))

nums = [3, 3, 1, 3]
print(s.findMin(nums))

nums = [1, 3, 3]
print(s.findMin(nums))
