# 1218. 最长定差子序列
from typing import List
from collections import defaultdict


class Solution:
    # def longestSubsequence(self, arr: List[int], difference: int) -> int:
    #     dp = defaultdict(int)
    #     for num in arr:
    #         dp[num] = dp[num-difference] + 1
    #     return max(dp.values())

    # 动态规划：超时
    # def longestSubsequence(self, arr: List[int], difference: int) -> int:
    #     n = len(arr)
    #     dp = [1] * n
    #     for i in range(n):
    #         for j in range(i):
    #             if arr[j] + difference == arr[i]:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #     return max(dp)

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for a in arr:
            dp[a] = dp[a-difference] + 1
        return max(dp.values())


s = Solution()
arr = [1,2,3,4]
difference = 1
print(s.longestSubsequence(arr, difference))

arr = [1,3,5,7]
difference = 1
print(s.longestSubsequence(arr, difference))

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(s.longestSubsequence(arr, difference))

arr = [3,4,-3,-2,-4]
difference = -5
print(s.longestSubsequence(arr, difference))
