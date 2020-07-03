# 二分查找
from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low >> 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def first_search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[right] == target:
            return right
        return -1

    def last_search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right + 1 >> 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[right] == target:
            return right
        return -1




s = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(s.search(nums, target))

nums = [-1,0,3,5,9,12]
target = 2
print(s.search(nums, target))

nums = [5]  # 加等号的原因
target = 5
print(s.search(nums, target))

print('查找第一个值等于给定值的元素')
###
nums = [0, 1, 1, 1, 2, 3]
target = 1
print(s.first_search(nums, target))

nums = [0, 1, 1, 1, 2, 4]
target = 5
print(s.first_search(nums, target))

nums = []
target = 5
print(s.first_search(nums, target))

nums = [5]
target = 5
print(s.first_search(nums, target))

nums = [4, 4, 4, 4, 7, 8]
target = 4
print(s.first_search(nums, target))

nums = [4, 4, 4, 4, 7, 8]
target = 8
print(s.first_search(nums, target))


print('查找最后一个值等于给定值的元素')
###
nums = [0, 1, 1, 1, 2, 3]
target = 1
print(s.last_search(nums, target))

nums = [0, 1, 1, 1, 2, 4]
target = 5
print(s.last_search(nums, target))

nums = []
target = 5
print(s.last_search(nums, target))

nums = [5]
target = 5
print(s.last_search(nums, target))

nums = [4, 4, 4, 4, 7, 8, 8]
target = 8
print(s.last_search(nums, target))

nums = [4, 4, 4, 4, 7, 8]
target = 4
print(s.last_search(nums, target))


