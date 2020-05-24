# 幂
class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     return pow(x, n)

    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1.0
        if n == -1:
            return 1/x
        if n & 1:  # 奇数幂
            return self.myPow(x, n >> 1) ** 2 * x
        else:
            return self.myPow(x, n >> 1) ** 2


s = Solution()
x, n = 2.00000, 10
print(s.myPow(x, n))

x, n = 2.10000, 3
print(s.myPow(x, n))

x, n = 2.00000, -2
print(s.myPow(x, n))
