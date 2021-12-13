# 29.两数相除
class Solution:
    # def divide(self, dividend: int, divisor: int) -> int:
    #     res = int(dividend / divisor)
    #     if -2**31 <= res <= 2**31-1:
    #         return res
    #     return 2**31-1

    # def divide(self, dividend: int, divisor: int) -> int:
    #     if dividend * divisor > 0:
    #         res = dividend // divisor
    #     else:
    #         res = -1 * (abs(dividend) // abs(divisor))
    #     if -2 ** 31 <= res <= 2 ** 31 - 1:
    #         return res
    #     return 2 ** 31 - 1

    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor)
        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res
        return 2 ** 31 - 1


s = Solution()
dividend = 10
divisor = 3
print(s.divide(dividend, divisor))

dividend = 7
divisor = -3
print(s.divide(dividend, divisor))

dividend = -2147483648
divisor = -1
print(s.divide(dividend, divisor))
