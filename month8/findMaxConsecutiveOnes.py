# 最大连续 1 的个数
from typing import List


class Solution:
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     res, count = 0, 0
    #     for num in nums:
    #         if num:
    #             count += 1
    #         else:
    #             res = max(res, count)
    #             count = 0
    #     return max(res, count)

    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     return len(max(''.join(map(str, nums)).split('0')))

    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     res = 0
    #     i = 0
    #     for j, num in enumerate(nums):
    #         if not num:
    #             res = max(res, j-i)
    #             i = j + 1
    #     if nums[-1]:
    #         res = max(res, len(nums)-i)
    #     return res

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for num in nums:
            if num:
                count += 1
            else:
                res = max(res, count)
                count = 0
        if nums[-1]:
            res = max(res, count)
        return res




s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))

