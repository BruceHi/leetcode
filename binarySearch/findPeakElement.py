# 寻找峰值，要求时间复杂度是 O（log n）
from typing import List


class Solution:

    # 线性扫描，时间复杂度 O(n), 默认相邻的不相同
    # def findPeakElement(self, nums: List[int]) -> int:
    #     for i in range(len(nums) - 1):
    #         if nums[i] > nums[i+1]:
    #             return i
    #     return len(nums) - 1

    # 二分查找，时间复杂度 O(n log n)
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