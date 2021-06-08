# 279. 完全平方数
from math import sqrt


class Solution:
    # def numSquares(self, n: int) -> int:
    #     nums = [i**2 for i in range(1, int(sqrt(n))+1)]
    #     dp = [float('inf')] * (n + 1)
    #     dp[0] = 0
    #     for i in range(1, n+1):
    #         for num in nums:
    #             if i - num >= 0:
    #                 dp[i] = min(dp[i-num] + 1, dp[i])  # 1要写里面
    #     return dp[n]

    #
    # 由于 nums 是按顺序构造的，所以有些可以提前终止。
    # def numSquares(self, n: int) -> int:
    #     nums = [i**2 for i in range(1, int(sqrt(n))+1)]
    #     dp = [float('inf')] * (n + 1)
    #     dp[0] = 0
    #     for i in range(1, n+1):
    #         for num in nums:
    #             if i < num:
    #                 break
    #             dp[i] = min(dp[i], dp[i-num] + 1)  # 1要写里面
    #     return dp[n]

    # def numSquares(self, n: int) -> int:
    #     nums = [i**2 for i in range(1, int(sqrt(n))+1)]
    #     dp = [float('inf')] * (n+1)
    #     dp[0] = 0
    #     for i in range(1, n+1):
    #         for num in nums:
    #             if i < num:
    #                 break
    #             dp[i] = min(dp[i], dp[i-num]+1)
    #     return dp[n]

    def numSquares(self, n: int) -> int:
        nums = [x*x for x in range(1, int(sqrt(n))+1)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for num in nums:
            for x in range(num, n+1):
                dp[x] = min(dp[x], dp[x-num]+1)
        return dp[n]


s = Solution()
print(s.numSquares(12))

print(s.numSquares(13))

print(s.numSquares(4))

print(s.numSquares(8))
