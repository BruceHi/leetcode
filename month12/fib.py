# 剑指 offer 10-1. 斐波那契数列
# 答案需要取模 1e9+7（1000000007）
from functools import lru_cache


class Solution:
    # @lru_cache(None)
    # def fib(self, n: int) -> int:
    #     if not n:
    #         return 0
    #     if n == 1:
    #         return 1
    #     return self.fib(n-1) + self.fib(n-2)

    # def fib(self, n: int) -> int:
    #     @lru_cache(None)
    #     def dfs(n):
    #         if not n:
    #             return 0
    #         if n == 1:
    #             return 1
    #         return dfs(n-1) + dfs(n-2)
    #     return dfs(n) % int(1e9+7)  # 科学计数法，返回结果是浮点数类型

    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = a+b, a
        return a % 1000000007


s = Solution()
n = 2
print(s.fib(n))

n = 5
print(s.fib(n))
