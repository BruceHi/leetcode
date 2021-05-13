# 31. 下一个排列
from typing import List
from itertools import permutations


class Solution:
    #     1. 其实就是从数组倒着查找，找到nums[i] 比nums[i+1]小的时候。注意：此时 nums[i+1:]是逆序的。
    #     2. 就将nums[i]跟nums[i+1]到nums[nums.length - 1]当中找到一个最小的比nums[i]大的元素交换。
    #     从右往左遍历，第一次出现的即是比nums[i]大的最小值。
    #     3. 交换后，再把nums[i+1]到nums[nums.length-1]排序，就ok了

    # def nextPermutation(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     if nums == sorted(nums, reverse=True):
    #         nums.sort()
    #         return
    #     idx = 0
    #     for i in range(len(nums)-1, 0, -1):
    #         if nums[i] > nums[i-1]:
    #             idx = i - 1
    #             break
    #     val = min(filter(lambda x: x > nums[idx], nums[idx+1:]))
    #     # j = nums[idx+1:].index(val)  # 错误，此时 为 0 的位置是从 idx + 1 算起。
    #     j = nums.index(val, idx+1)
    #     nums[idx], nums[j] = val, nums[idx]
    #     nums[idx+1:] = sorted(nums[idx+1:])

    # 两遍扫描
    # def nextPermutation(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     # i = n - 1
    #     # while i and nums[i-1] >= nums[i]:
    #     #     i -= 1
    #     # i -= 1
    #     # 注意与上面的区别
    #     i = n - 2
    #     while i >= 0 and nums[i] >= nums[i+1]:
    #         i -= 1
    #
    #     if i >= 0:  # 排除逆序的情况
    #         j = n - 1
    #         while nums[j] <= nums[i]:
    #             j -= 1
    #         nums[i], nums[j] = nums[j], nums[i]
    #
    #     left, right = i + 1, n - 1
    #     while left < right:
    #         nums[left], nums[right] = nums[right], nums[left]
    #         left, right = left + 1, right - 1

        # nums[:] = nums[:i+1] + list(reversed(nums[i+1:]))

    # def nextPermutation(self, nums: List[int]) -> None:
    #     if nums == sorted(nums, reverse=True):
    #         nums.sort()
    #         return
    #     n = len(nums)
    #
    #     i = n - 1
    #     while i-1 >= 0 and nums[i-1] >= nums[i]:
    #         i -= 1
    #     i -= 1
    #
    #     val = min(filter(lambda x: x > nums[i], nums[i+1:]))
    #     j = nums.index(val, i+1)
    #     nums[i], nums[j] = val, nums[i]
    #     nums[i+1:] = sorted(nums[i+1:])

    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        i = n - 1
        while i - 1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1



s = Solution()
nums = [1, 2, 3]
s.nextPermutation(nums)
print(nums)

nums = [3,2,1]
s.nextPermutation(nums)
print(nums)

nums = [1,1,5]
s.nextPermutation(nums)
print(nums)

nums = [1]
s.nextPermutation(nums)
print(nums)