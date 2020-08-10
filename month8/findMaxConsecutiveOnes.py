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

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(max(''.join(map(str, nums)).split('0')))


s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))

