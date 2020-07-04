# 在排序数组中查找元素的第一个和最后一个位置
from typing import List


class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = left + right >> 1
    #         tmp = nums[mid]
    #         if tmp < target:
    #             left = mid + 1
    #         elif tmp > target:
    #             right = mid - 1
    #         else:
    #             left = mid
    #             while left != 0 and nums[left] == nums[left-1]:
    #                 left -= 1
    #
    #             right = mid
    #             while right != len(nums)-1 and nums[right] == nums[right + 1]:
    #                 right += 1
    #
    #             return [left, right]
    #     return [-1, -1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[right] != target:
            return [-1, -1]
        res = [right]

        right = len(nums) - 1
        while left < right:
            mid = 1 + left + right >> 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        res += [right]
        return res


s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums, target))

nums = [5, 7, 7, 8, 8, 10]
target = 6
print(s.searchRange(nums, target))

nums = [1, 1, 1, 1,1,1]
target = 1
print(s.searchRange(nums, target))

nums = [1]
target = 1
print(s.searchRange(nums, target))

nums = []
target = 1
print(s.searchRange(nums, target))

nums = [1,1]
target = 1
print(s.searchRange(nums, target))