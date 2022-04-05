# 172.阶乘后的零
from functools import reduce
from math import factorial


class Solution:

    # # 0 的阶乘为 1。
    # def trailingZeroes(self, n: int) -> int:
    #     if not n:
    #         return 0
    #     num = reduce(lambda x, y: x*y, range(1, n+1))
    #     num_str = str(num)
    #     if num_str.endswith('0'):
    #         count = 0
    #         for c in reversed(num_str):
    #             if c == '0':
    #                 count += 1
    #             else:
    #                 break
    #         return count
    #     return 0

    # def trailingZeroes(self, n: int) -> int:
    #     num = factorial(n)
    #     count = 0
    #     while not num % 10:  # 不能整除 10 的，退出
    #         count += 1
    #         num //= 10
    #     return count

    # 求取 5 出现的个数
    # 因为 5 * 2 = 10，
    # https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/xiang-xi-tong-su-de-si-lu-fen-xi-by-windliang-3/
    # def trailingZeroes(self, n: int) -> int:
    #     count = 0
    #     while n > 0:
    #         count += n // 5
    #         n //= 5
    #     return count

    # def trailingZeroes(self, n: int) -> int:
    #     num = factorial(n)
    #     res = 0
    #     while num % 10 == 0:
    #        res += 1
    #        num //= 10
    #     return res

    # def trailingZeroes(self, n: int) -> int:
    #     res = 0
    #     for i in range(5, n+1, 5):
    #         while i % 5 == 0:
    #             res += 1
    #             i //= 5
    #     return res

    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            res += n // 5
            n //= 5
        return res


s = Solution()
print(s.trailingZeroes(0))

print(s.trailingZeroes(3))

print(s.trailingZeroes(5))

print(s.trailingZeroes(7))  # 结果为 5040，尾数中有 1 个 0

print(f'{7 * 6 * 5 * 4 * 3 * 2}')
