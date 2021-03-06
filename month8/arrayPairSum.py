# 数组拆分 I
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res

    # def arrayPairSum(self, nums: List[int]) -> int:
    #     nums.sort()
    #     res = 0
    #     for i, num in enumerate(nums):
    #         if not i & 1:
    #             res += num
    #     return res


s = Solution()
print(s.arrayPairSum([1, 4, 3, 2]))
