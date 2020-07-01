# 长度最小的子数组
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(end - start +1, ans)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans


obj = Solution()
s = 7
nums = [2,3,1,2,4,3]
print(obj.minSubArrayLen(s, nums))