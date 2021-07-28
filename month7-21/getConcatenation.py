from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


s = Solution()
nums = [1,2,1]
print(s.getConcatenation(nums))

nums = [1,3,2,1]
print(s.getConcatenation(nums))
