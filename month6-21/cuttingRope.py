# 剑指 offer 14-2：剪绳子
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n-1
        a, b = divmod(n, 3)
        if b == 0:
            return 3 ** a % 1000000007
        if b == 1:
            return 3**(a-1) * 4 % 1000000007
        return 3 ** a * 2 % 1000000007


s = Solution()
n = 2
print(s.cuttingRope(n))

n = 10
print(s.cuttingRope(n))

n = 11
print(s.cuttingRope(n))
