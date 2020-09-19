# 搜索插入位置
from typing import List
import bisect


class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     return bisect.bisect_left(nums, target)

    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     return bisect.bisect_left(nums, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:  # 特判，因为后面的 left 取值范围是 [0, len(nums) - 1]
            return len(nums)

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left





s = Solution()
print(s.searchInsert([1,3,5,6], 5))

print(s.searchInsert([1,3,5,6], 2))

print(s.searchInsert([1,3,5,6], 7))

print(s.searchInsert([1,3,5,6], 0))
