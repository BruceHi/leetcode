# 747. 至少是其他数字两倍的最大数
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0
        if nums.count(max(nums)) > 1:
            return -1
        m = max(nums)
        for num in nums:
            if num != m and m < num * 2:
                return -1
        return nums.index(m)


s = Solution()
nums = [3,6,1,0]
print(s.dominantIndex(nums))

nums = [1,2,3,4]
print(s.dominantIndex(nums))

nums = [1]
print(s.dominantIndex(nums))
