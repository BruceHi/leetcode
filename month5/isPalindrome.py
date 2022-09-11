# 验证回文数
class Solution:

    # 反转
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
    #     n, res = x, 0
    #     while n:
    #         res = res * 10 + n % 10
    #         n //= 10
    #     return x == res

    # （后）部分反转
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or x and not x % 10:
    #         return False
    #
    #     res = 0
    #     while x > res:
    #         res = res * 10 + x % 10
    #         x //= 10
    #
    #     return x == res or x == res // 10

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or not x % 10:
    #         return False
    #     res = 0
    #     while res < x:
    #         res = res * 10 + x % 10
    #         x //= 10
    #     return x == res or x == res // 10

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or x and not x % 10:
    #         return False
    #     n = 0
    #     while x > n:
    #         n = n * 10 + x % 10
    #         x //= 10
    #     return x == n or x == n // 10

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or x and x % 10 == 0:
    #         return False
    #     n = 0
    #     while x > n:
    #         n = n * 10 + x % 10
    #         x //= 10
    #     return x == n or x == n // 10

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or x > 0 and x % 10 == 0:
    #         return False
    #     res = 0
    #     while x > res:
    #         res = res * 10 + x % 10
    #         x //= 10
    #     return x == res or x == res // 10

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or x and x % 10 == 0:
    #         return False
    #     res = 0
    #     while x > res:
    #         res = res * 10 + x % 10
    #         x //= 10
    #     return x == res or res // 10 == x

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or x and x % 10 == 0:
    #         return False
    #     res = 0
    #     while res < x:
    #         res = res * 10 + x % 10
    #         x //= 10
    #     return res == x or res // 10 == x

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or x and x % 10 == 0:
    #         return False
    #     res = 0
    #     while res < x:
    #         res = res * 10 + x % 10
    #         x //= 10
    #     return res == x or res // 10 == x

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x and x % 10 == 0:
            return False
        res = 0
        while x > res:
            res = res * 10 + x % 10
            x //= 10
        return res == x or res // 10 == x


s = Solution()
num = 121
print(s.isPalindrome(num))

s = Solution()
num = -121
print(s.isPalindrome(num))

s = Solution()
num = 10
print(s.isPalindrome(num))

num = 4
print(s.isPalindrome(num))

num = 0
print(s.isPalindrome(num))

num = 1001
print(s.isPalindrome(num))
