# 整数拆分
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        a, b = divmod(n, 3)
        if not b:
            return 3 ** a
        if b == 1:
            return 3 ** (a-1) * 4
        if b == 2:
            return 3 ** a * b


s = Solution()
print(s.integerBreak(2))

print(s.integerBreak(10))
