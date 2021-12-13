# 372. 超级次方
from typing import List


class Solution:
    # 超时
    # def superPow(self, a: int, b: List[int]) -> int:
    #     num = 0
    #     for n in b:
    #         num = num * 10 + n
    #     return a ** num % 1337

    # 快速幂 超时
    # def superPow(self, a: int, b: List[int]) -> int:
    #     def power(x, y):
    #         if y == 0:
    #             return 1
    #         if y == 1:
    #             return x
    #         tmp = power(x, y // 2)
    #         if y & 1:
    #             return tmp * tmp * x
    #         return tmp * tmp
    #
    #     num = 0
    #     for n in b:
    #         num = num * 10 + n
    #     return power(a, num) % 1337

    # 快速幂 + 递归
    def superPow(self, a: int, b: List[int]) -> int:
        def power(x, y):
            if y == 0:
                return 1
            if y == 1:
                return x
            tmp = power(x, y // 2)
            if y & 1:
                return tmp * tmp * x
            return tmp * tmp

        def dfs(i):
            if i == -1:
                return 1
            return power(dfs(i-1), 10) * power(a, b[i]) % 1337

        return dfs(len(b)-1)


s = Solution()
a = 2
b = [3]
print(s.superPow(a, b))

a = 2
b = [1,0]
print(s.superPow(a, b))

a = 1
b = [4,3,3,8,5,2]
print(s.superPow(a, b))

a = 2147483647
b = [2,0,0]
print(s.superPow(a, b))
