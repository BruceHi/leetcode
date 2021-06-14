# 263. 丑数
class Solution:
    # def isUgly(self, n: int) -> bool:
    #     if n < 1:
    #         return False
    #     while n != 1:
    #         if n % 2 == 0:
    #             n //= 2
    #         elif n % 3 == 0:
    #             n //= 3
    #         elif n % 5 == 0:
    #             n //= 5
    #         else:
    #             return False
    #     return True

    # 另一种写法
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        return n == 1


s = Solution()
n = 6
print(s.isUgly(n))

n = 8
print(s.isUgly(n))

n = 14
print(s.isUgly(n))

n = 1
print(s.isUgly(n))
