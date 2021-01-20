# 977. 有序数组的平方
from typing import List


class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted(map(lambda x: x * x, nums))

    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num * num for num in nums])


s = Solution()
nums = [-4,-1,0,3,10]
print(s.sortedSquares(nums))

nums = [-7,-3,2,3,11]
print(s.sortedSquares(nums))
