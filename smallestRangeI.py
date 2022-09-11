# 908. 最小差值1
from typing import List


class Solution:
    # def smallestRangeI(self, nums: List[int], k: int) -> int:
    #     a, b = min(nums), max(nums)
    #     if a + k >= b - k:
    #         return 0
    #     return (b - k) - (a + k)

    # def smallestRangeI(self, nums: List[int], k: int) -> int:
    #     small, big = min(nums), max(nums)
    #     if small + k >= big - k:
    #         return 0
    #     return big - k - (small + k)

    # def smallestRangeI(self, nums: List[int], k: int) -> int:
    #     min_v, max_v = min(nums), max(nums)
    #     if len(nums) == 1 or min_v + k >= max_v - k:
    #         return 0
    #     return max_v - k - (min_v + k)

    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_v, max_v = min(nums), max(nums)
        if min_v + k >= max_v - k:
            return 0
        return max_v - k - (min_v + k)


s = Solution()
nums = [1]
k = 0
print(s.smallestRangeI(nums, k))

nums = [0,10]
k = 2
print(s.smallestRangeI(nums, k))

nums = [1,3,6]
k = 3
print(s.smallestRangeI(nums, k))
