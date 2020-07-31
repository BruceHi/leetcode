# 爬楼梯


class Solution:
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     f = [0] * (n + 1)
    #     f[1], f[2] = 1, 2
    #     for i in range(3, n+1):  # 从前往后迭代求解，但想法是自底向上，即直至目标。
    #         f[i] = f[i-1] + f[i-2]
    #
    #     return f[n]
    #

    # def climbStairs(self, n: int) -> int:
    #     x, y = 1, 1
    #     for _ in range(1, n):
    #         x, y = y, x+y
    #     return y

    # def climbStairs(self, n: int) -> int:
    #     dp = [1, 1]
    #     for i in range(2, n+1):
    #         dp.append(dp[i-1] + dp[i-2])
    #     return dp[n]


        # 递归
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 递归，超时
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)

    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     dp = 2
    #     dp_old = 1
    #     for i in range(2, n):
    #         tmp = dp
    #         dp = dp + dp_old
    #         dp_old = tmp
    #     return dp

    # def climbStairs(self, n: int) -> int:
    #     dp, dp_old = 1, 1
    #     for i in range(1, n):
    #         dp, dp_old = dp + dp_old, dp
    #     return dp

    def climbStairs(self, n: int) -> int:
        x, y = 1, 1
        for _ in range(2, n):
            x, y = y, x + y
        return y


s = Solution()
print(s.climbStairs(1))
print(s.climbStairs(2))

print(s.climbStairs(3))
