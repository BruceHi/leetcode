# 剑指 offer 21.调整数组顺序使奇数位于偶数前面
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0
        for j, num in enumerate(nums):
            if num & 1:
                nums[i], nums[j] = num, nums[i]
                i += 1
        return nums


s = Solution()
nums = [1,2,3,4]
print(s.exchange(nums))

nums = [1]
print(s.exchange(nums))

nums = []
print(s.exchange(nums))

nums = [2]
print(s.exchange(nums))
