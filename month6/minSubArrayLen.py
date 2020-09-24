# 长度最小的连续子数组
# 注意并不是要求里面数字是连续的

from typing import List


class Solution:
    # def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #
    #     n = len(nums)
    #     ans = n + 1
    #     start, end = 0, 0
    #     total = 0
    #     while end < n:
    #         total += nums[end]
    #         while total >= s:
    #             ans = min(end - start + 1, ans)
    #             total -= nums[start]
    #             start += 1
    #         end += 1
    #
    #     return 0 if ans == n + 1 else ans

    # 暴力法，超时
    # def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #
    #     n = len(nums)
    #     res = n + 1
    #     for i in range(n):
    #         total = 0
    #         for j in range(i, n):  # 能用 for 循环尽量用 for 循环
    #             total += nums[j]
    #             if total >= s:
    #                 res = min(res, j - i + 1)
    #                 break
    #     return 0 if res == n + 1 else res
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        res = n + 1
        i, j = 0, 0
        total = 0
        while j < n:
            total += nums[j]
            while total >= s:
                res = min(res, j - i + 1)
                total -= nums[i]
                i += 1
            j += 1
        return 0 if res == n + 1 else res



obj = Solution()
s = 7
nums = [2,3,1,2,4,3]
print(obj.minSubArrayLen(s, nums))

s = 100
nums = []
print(obj.minSubArrayLen(s, nums))

s = 11
nums = [1,2,3,4,5]
print(obj.minSubArrayLen(s, nums))

s = 3
nums = []
print(obj.minSubArrayLen(s, nums))
