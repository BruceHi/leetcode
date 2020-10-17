# 第三大的数，要求时间复杂度是 O（n）
from typing import List


class Solution:
    # def thirdMax(self, nums: List[int]) -> int:
    #     nums = list(set(nums))
    #     n = len(nums)
    #     if n < 3:
    #         return max(nums)
    #     self.partition(nums, 0, n-1, 3)
    #     return nums[2]
    #
    # def partition(self, nums, left, right, k):
    #     if left > right:
    #         return
    #     pivot, i = nums[right], left
    #     for j in range(left, right):
    #         if nums[j] > pivot:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             i += 1
    #     nums[i], nums[right] = pivot, nums[i]
    #     if i+1 < k:
    #         return self.partition(nums, i+1, right, k)
    #     elif i+1 > k:
    #         return self.partition(nums, left, i-1, k)
    #     return i


    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        return sorted(nums, reverse=True)[2]


s = Solution()
arr = [3, 2, 1]
print(s.thirdMax(arr))

arr = [1, 2]
print(s.thirdMax(arr))

arr = [2, 2, 3, 1]
print(s.thirdMax(arr))

arr = [2, 2, 3, 3]
print(s.thirdMax(arr))

arr = [1,2,2,5,3,5]
print(s.thirdMax(arr))
