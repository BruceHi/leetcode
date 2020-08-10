# 寻找数组的中心索引
from typing import List
from collections import deque


class Solution:

    # 可以通过，但太麻烦了
    # def pivotIndex(self, nums: List[int]) -> int:
    #     if not nums:
    #         return -1
    #     n = len(nums)
    #     prefix = [0]
    #     for num in nums:
    #         prefix.append(prefix[-1] + num)
    #
    #     suffix = deque([0])
    #     for num in nums[::-1]:
    #         suffix.appendleft(suffix[0] + num)
    #
    #     for i in range(n):
    #         if prefix[i] == suffix[i+1]:
    #             return i
    #     return -1

    def pivotIndex(self, nums: List[int]) -> int:
        sum_val = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == sum_val - left_sum - num:
                return i
            left_sum += num
        return -1


s = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(s.pivotIndex(nums))

nums = [1, 2, 3]
print(s.pivotIndex(nums))

nums = [1, 4, 3, 2]
print(s.pivotIndex(nums))

nums = [-1,-1,-1,-1,-1,0]
print(s.pivotIndex(nums))

nums = [-1,-1,-1,-1,-1,-1]
print(s.pivotIndex(nums))

nums = [-1,-1,-1,0,1,1]
print(s.pivotIndex(nums))

nums = [-1,-1,0,1,1,0]
print(s.pivotIndex(nums))