# 剑指 offer 45. 把数组排成最小的数
from typing import List
from functools import cmp_to_key


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        cmp = lambda x, y: int(y+x) - int(x+y)
        return ''.join(sorted(map(str, nums), key=cmp_to_key(cmp), reverse=True))


s = Solution()
nums = [10,2]
print(s.minNumber(nums))

nums = [3,30,34,5,9]
print(s.minNumber(nums))
