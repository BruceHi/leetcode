# 剑指 Offer 53 - II. 0～n-1中缺失的数字
# 长度为 n-1
# 递增排序数组
from typing import List


class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
    #     if nums[0] != 0:
    #         return 0
    #     for i, num in enumerate(nums[:-1]):
    #         if num + 1 != nums[i+1]:
    #             return num + 1
    #     return nums[-1] + 1

    # # 直接遍历，和上面方法一样
    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     for i in range(n):
    #         if nums[i] != i:
    #             return i
    #     return n

    # 二分法，时间复杂度为 O(logn)，
    # https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/solution/mian-shi-ti-53-ii-0n-1zhong-que-shi-de-shu-zi-er-f/
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + j >> 1
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i


s = Solution()
nums = [0,1,3]
print(s.missingNumber(nums))

nums = [0,1,2,3,4,5,6,7,9]
print(s.missingNumber(nums))

nums = [0,1,2]
print(s.missingNumber(nums))
