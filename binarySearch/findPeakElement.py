# 寻找峰值，要求时间复杂度是 O（log n）
from typing import List


class Solution:
    # def findPeakElement(self, nums: List[int]) -> int:
    #     if len(nums) <= 1:
    #         return 0
    #     for i in range(len(nums)):
    #         if i == 0 and nums[i] > nums[i+1]:
    #             return i
    #         if i == len(nums)-1 and nums[i-1] < nums[i]:
    #             return i
    #         if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
    #             return i

    # def findPeakElement(self, nums: List[int]) -> int:
    #     for i in range(len(nums) - 1):
    #         if nums[i] > nums[i+1]:
    #             return i
    #     return len(nums) - 1

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right >> 1
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return right


s = Solution()
nums = [1,2,3,1]
print(s.findPeakElement(nums))

nums = [1,2,1,3,5,6,4]
print(s.findPeakElement(nums))

nums = [1,2]
print(s.findPeakElement(nums))

nums = []
print(s.findPeakElement(nums))