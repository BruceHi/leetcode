# 寻找旋转排序数组中的最小值
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]

    # 找到最大值，失败
    # def findMax(self, nums: List[int]) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = left + right >> 1
    #         if nums[mid] > nums[left]:
    #             left = mid
    #         else:
    #             right = mid - 1
    #     return nums[right]



s = Solution()
nums = [3,4,5,1,2]
print(s.findMin(nums))
# print(s.findMax(nums))

nums = [4,5,6,7,0,1,2]
print(s.findMin(nums))
# print(s.findMax(nums))

nums = [1, 2, 3]
print(s.findMin(nums))
# print(s.findMax(nums))

nums = [3, 2, 1]
print(s.findMin(nums))
# print(s.findMax(nums))

nums = [2, 3, 4, 5, 1]
print(s.findMin(nums))
# print(s.findMax(nums))
