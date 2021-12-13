# 面试题 08.11 硬币
class Solution:
    def waysToChange(self, n: int) -> int:
        if n == 0:
            return 0
        coins = [1, 5, 10, 25]
        dp = [0] * (n+1)
        dp[0] = 1

        for c in coins:
            for i in range(c, n+1):
                dp[i] += dp[i-c]
        return dp[n] % 1000000007


s = Solution()
n = 5
print(s.waysToChange(n))

n = 10
print(s.waysToChange(n))

n = 0
print(s.waysToChange(n))
