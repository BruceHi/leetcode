# 326. 3 的幂
from math import log


class Solution:
    # # 递归
    # def isPowerOfThree(self, n: int) -> bool:
    #     if n == 1:
    #         return True
    #     if not n:
    #         return False
    #     if n % 3:
    #         return False
    #     return self.isPowerOfThree(n//3)

    # 迭代
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

    # 使用公式，返回 float，将结果 对 1 求余（%1），若原来是整数浮点型（比如：2.0）结果是 0.0，返回 False，否则返回 True
    # log 第一个参数不能是 0 或 负数
    # 使用 公式错误，比如 243 是 3 的 5 次方，结果返回 4.999999
    # def isPowerOfThree(self, n: int) -> bool:
    #     if n < 1:
    #         return False
    #     return not log(n, 3) % 1


s = Solution()
n = 27
print(s.isPowerOfThree(n))

n = 0
print(s.isPowerOfThree(n))

n = 9
print(s.isPowerOfThree(n))

n = 45
print(s.isPowerOfThree(n))

n = 243
print(s.isPowerOfThree(n))

print(log(243, 3))
