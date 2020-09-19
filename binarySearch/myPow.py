# 幂
class Solution:
    # def myPow(self, x: float, n: int) -> float:
        # return pow(x, n)
        # return x**n

    # def myPow(self, x: float, n: int) -> float:
    #     if n == 1:
    #         return x
    #     if n == 0:
    #         return 1.0
    #     if n == -1:
    #         return 1/x
    #     y = self.myPow(x, n >> 1)
    #     if n & 1:
    #         return y * y * x
    #     return y * y

    # def myPow(self, x: float, n: int) -> float:
    #     res, tmp, m = 1.0, x, n
    #     n = -n if n < 0 else n
    #     while n:
    #         if n & 1:
    #             res *= tmp
    #         n >>= 1
    #         tmp *= tmp
    #     return res if m >= 0 else 1/res

    # def myPow(self, x: float, n: int) -> float:
    #     res, tmp = 1.0, n
    #     if n < 0:
    #         n = -n
    #     while n:
    #         if n & 1:
    #             res *= x
    #         n >>= 1
    #         x *= x
    #     return res if tmp >= 0 else 1/res

    # def myPow(self, x: float, n: int) -> float:
    #     if not n:
    #         return 1.0
    #     if n == 1:
    #         return x
    #     if n == -1:
    #         return 1 / x
    #     y = self.myPow(x, n >> 1)
    #     if n & 1:
    #         return y * y * x
    #     return y * y

    # def myPow(self, x: float, n: int) -> float:
    #     sign = 1 if n > 0 else -1
    #     n = n if n > 0 else -n
    #     res = 1.0
    #     while n:
    #         if n & 1:
    #             res *= x
    #         x *= x
    #         n >>= 1
    #     return res if sign == 1 else 1 / res

    def myPow(self, x: float, n: int) -> float:
        sign = 1 if n > 0 else -1
        n = n if n > 0 else -n
        res = 1.0
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res if sign == 1 else 1 / res


s = Solution()
x, n = 2.00000, 10
print(s.myPow(x, n))

x, n = 2.10000, 3
print(s.myPow(x, n))

x, n = 2.00000, -2
print(s.myPow(x, n))

x, n = 2.00000, 0
print(type(s.myPow(x, n)))