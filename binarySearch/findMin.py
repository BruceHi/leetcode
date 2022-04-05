# 153.寻找旋转排序数组中的最小值
from typing import List


class Solution:
    # def findMin(self, nums: List[int]) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = left + right >> 1
    #         if nums[mid] > nums[right]:
    #             left = mid + 1
    #         else:
    #             right = mid
    #     return nums[right]

    # # # 找到最大值
    # def findMin(self, nums: List[int]) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = left + right + 1 >> 1  # 注意要加 1，回头再看看
    #         if nums[left] > nums[mid]:
    #             right = mid - 1
    #         else:
    #             left = mid
    #     return nums[right]

    # def findMin(self, nums: List[int]) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = left + right >> 1
    #         if nums[mid] > nums[right]:
    #             left = mid + 1
    #         else:
    #             right = mid
    #     return nums[left]

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + right >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


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

# 下面是错误示例，都说了是旋转排序，肯定不能是递减的啊
# nums = [3, 2, 1]
# print(s.findMin(nums))
# print(s.findMax(nums))

nums = [2, 3, 4, 5, 1]
print(s.findMin(nums))
# print(s.findMax(nums))
