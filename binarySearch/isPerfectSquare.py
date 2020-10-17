# 有效的完全平方数
from math import sqrt


class Solution:
    # def isPerfectSquare(self, num: int) -> bool:
    #     left, right = 1, num
    #     while left <= right:
    #         mid = left + right >> 1
    #         tmp = mid * mid
    #         if tmp == num:
    #             return True
    #         elif tmp < num:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return False

    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = left + right >> 1
            if mid ** 2 == num:
                return True
            if mid ** 2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


s = Solution()
print(s.isPerfectSquare(16))

print(s.isPerfectSquare(14))

print(s.isPerfectSquare(1))

print(s.isPerfectSquare(9))