# 34. 在排序数组中查找元素的第一个和最后一个位置
from typing import List
import bisect


class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     if not nums:
    #         return [-1, -1]
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = left + right >> 1
    #         if nums[mid] < target:
    #             left = mid + 1
    #         else:
    #             right = mid
    #     if nums[right] != target:
    #         return [-1, -1]
    #     res = [right]
    #
    #     right = len(nums) - 1  # 隐含条件是 left = right
    #     while left < right:
    #         mid = left + right + 1 >> 1
    #         if target < nums[mid]:
    #             right = mid - 1
    #         else:
    #             left = mid
    #     res += [right]
    #
    #     return res

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     left = bisect.bisect_left(nums, target)
    #     if left == len(nums) or nums[left] != target:
    #         return [-1, -1]
    #     right = bisect.bisect(nums, target) - 1
    #     # right = left + bisect.bisect(nums[left:], target) - 1
    #     return [left, right]


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        # 寻找左边界
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target:
            return [-1, -1]
        res = [left]

        # 寻找右边界，注意此时的 left 是左边界的索引值
        right = len(nums) - 1
        while left < right:
            mid = left + right + 1 >> 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        res.append(left)
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

nums = [1, 3]
target = 1
print(s.searchRange(nums, target))

nums = [2,2]
target = 3
print(s.searchRange(nums, target))

nums = [4, 4]
target = 3
print(s.searchRange(nums, target))