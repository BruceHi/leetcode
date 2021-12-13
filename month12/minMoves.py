# 453.最小操作次数使元素相等
# 逆向思维，牛逼
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        res = 0
        for num in nums:
            res += num - min_num
        return res


s = Solution()
nums = [1, 2, 3]
print(s.minMoves(nums))

nums = [1, 1, 1]
print(s.minMoves(nums))
