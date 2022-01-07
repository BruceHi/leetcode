# 507. 完美数
from math import sqrt, isqrt


class Solution:
    # 超时
    # def checkPerfectNumber(self, num: int) -> bool:
    #     res = 0
    #     for i in range(1, num):
    #         if num % i == 0:
    #             res += i
    #     return res == num

    def checkPerfectNumber(self, num: int) -> bool:
        res = 1
        for i in range(2, isqrt(num)+1):
            if num % i == 0:
                res += i + num // i
        if sqrt(num) == int(num):
            res -= sqrt(num)
        return res == num


s = Solution()
num = 28
print(s.checkPerfectNumber(num))

num = 6
print(s.checkPerfectNumber(num))

num = 496
print(s.checkPerfectNumber(num))

num = 8128
print(s.checkPerfectNumber(num))

num = 2
print(s.checkPerfectNumber(num))

num = 99999991
print(s.checkPerfectNumber(num))
