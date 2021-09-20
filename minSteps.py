# 650. 只有两个键的键盘
from math import sqrt


class Solution:
    # dp[i] = min(dp[a]+b, ...) 其中 a*b = i
    # a > b 则 dp[a]+b <= dp[b]+a
    # def minSteps(self, n: int) -> int:
    #
    #     def two_factor(n):
    #         res = []
    #         for i in range(2, int(sqrt(n))+1):
    #             if n % i == 0:
    #                 res.append([n//i, i])  # 大的值放前面，
    #         return res
    #
    #     dp = [x for x in range(n+1)]
    #     dp[1] = 0
    #
    #     for i in range(2, n+1):
    #         for a, b in two_factor(i):
    #             dp[i] = min(dp[i], dp[a]+b)
    #     return dp[n]


    # def minSteps(self, n: int) -> int:
    #     def two_factor(n):
    #         res = []
    #         for i in range(1, int(sqrt(n))+1):
    #             if n % i == 0:
    #                 res.append([n//i, i])
    #         return res
    #
    #     dp = [float('inf')] * (n+1)
    #     dp[1] = 0
    #
    #     for i in range(2, n+1):
    #         for a, b in two_factor(i):
    #             dp[i] = min(dp[i], dp[a] + b)
    #             dp[i] = min(dp[i], dp[b] + a)
    #     return dp[n]

    # def minSteps(self, n: int) -> int:
    #     dp = [float('inf')] * (n+1)
    #     dp[1] = 0
    #
    #     for i in range(2, n+1):
    #         for j in range(1, int(sqrt(i))+1):
    #             if i % j == 0:
    #                 dp[i] = min(dp[i], dp[j] + i//j)
    #                 dp[i] = min(dp[i], dp[i//j] + j)
    #     return dp[n]

    # def minSteps(self, n: int) -> int:
    #     dp = [x for x in range(n+1)]
    #     dp[1] = 0
    #
    #     for i in range(2, n+1):
    #         for j in range(2, int(sqrt(i))+1):
    #             if i % j == 0:
    #                 dp[i] = min(dp[i], dp[i//j] + j)
    #     return dp[n]

    # 数学方法
    # 分解等于所有质因数的和
    def minSteps(self, n: int) -> int:
        res = 0
        i = 2
        while i * i <= n:
            while n % i == 0:  # 不断进行分解
                res += i
                n //= i
            i += 1
        # 剩余 1，说明完全除尽了
        if n > 1:
            res += n
        return res


s = Solution()
n = 1
print(s.minSteps(n))

n = 2
print(s.minSteps(n))

n = 3
print(s.minSteps(n))

n = 7
print(s.minSteps(n))

n = 8
print(s.minSteps(n))

n = 12
print(s.minSteps(n))

n = 24
print(s.minSteps(n))