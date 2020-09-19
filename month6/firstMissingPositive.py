# 缺失的第一个正整数
from typing import List


class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 1
    #     max_val = max(nums) if max(nums) > 0 else 0
    #     nums = set(nums)
    #     for num in range(max_val):
    #         if num + 1 not in nums:
    #             return num + 1
    #     return max_val + 1

    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     nums = set(nums)
    #     for i in range(n):
    #         if i + 1 not in nums:
    #             return i + 1
    #     return n + 1

    # # 使用了额外空间，空间复杂度是 O(n)
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     nums = set(nums)
    #     for i in range(1, n+2):
    #         if i not in nums:
    #             return i

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num-1] = -abs(nums[num-1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1




s = Solution()
a = [1,2,0]
print(s.firstMissingPositive(a))

a = [3,4,-1,1]
print(s.firstMissingPositive(a))

a = [7,8,9,11,12]
print(s.firstMissingPositive(a))

a = []
print(s.firstMissingPositive(a))

a = [-1, -2]
print(s.firstMissingPositive(a))