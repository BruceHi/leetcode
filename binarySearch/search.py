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