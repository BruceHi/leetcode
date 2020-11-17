# 下一个排列
from typing import List


class Solution:
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
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # i = n - 1
        # while i and nums[i-1] >= nums[i]:
        #     i -= 1
        # i -= 1
        # 注意与上面的区别
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:  # 排除逆序的情况
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

        # nums[:] = nums[:i+1] + list(reversed(nums[i+1:]))


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