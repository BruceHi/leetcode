# 75. 颜色分类
from typing import List
from collections import Counter


class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     nums.sort()

    # # 单指针，把 0 放前面，把 1 放前面
    # def sortColors(self, nums: List[int]) -> None:
    #     i = 0
    #     for j, num in enumerate(nums):
    #         if not num:
    #             nums[i], nums[j] = num, nums[i]
    #             i += 1
    #
    #     for j in range(i, len(nums)):
    #         if nums[j] == 1:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             i += 1

    # # 双指针，从前遍历
    # def sortColors(self, nums: List[int]) -> None:
    #     p0, p1 = 0, 0
    #     for i, num in enumerate(nums):
    #         if num == 1:
    #             nums[i], nums[p1] = nums[p1], num
    #             p1 += 1
    #         elif not num:
    #             nums[i], nums[p0] = nums[p0], num
    #             if p0 < p1:
    #                 nums[i], nums[p1] = nums[p1], nums[i]
    #             p0, p1 = p0 + 1, p1 + 1

    # 双指针，使用 Partition
    def sortColors(self, nums: List[int]) -> None:
        p0, p2 = 0, len(nums) - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if not nums[i]:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1



s = Solution()
nums = [2,0,2,1,1,0]
s.sortColors(nums)
print(nums)

nums = [2,0,2,1,1,0]
s.sortColors(nums)
print(nums)

nums = [1]
s.sortColors(nums)
print(nums)
