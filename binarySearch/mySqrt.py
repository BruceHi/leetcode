# x 的平方根
from math import sqrt


class Solution:
    # def mySqrt(self, x: int) -> int:
    #     return int(sqrt(x))

    # 二分法 结果为整数向下取整
    # def mySqrt(self, x: int) -> int:
    #     left, right = 0, x
    #     while left <= right:
    #         mid = (left + right) >> 1
    #         temp = mid ** 2
    #         if temp == x:
    #             return mid
    #         elif temp > x:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #
    #     return right

    # # 牛顿法
    # def mySqrt(self, x: int) -> int:
    #     r = x
    #     while r ** 2 - x >= 1:  # 设置精度，r 最终退出时，其平方与准确值之间小于 1。然后取整数部分即可。
    #         r = (r + x/r) / 2
    #     return int(r)

    # 二分法, 返回浮点数
    # def mySqrt(self, x: int) -> float:
    #     left, right = 0, x
    #     while right - left > 1e-6:  # 计算精度
    #         mid = (left + right) / 2
    #         temp = mid ** 2
    #         if temp == x:
    #             return mid
    #         elif temp > x:
    #             right = mid
    #         else:
    #             left = mid
    #
    #     return right * 1.0

    # def mySqrt(self, x: int) -> int:
    #     left, right = 0, x
    #     while left <= right:
    #         mid = left + (right - left >> 1)
    #         tmp = mid * mid
    #         if tmp == x:
    #             return mid
    #         elif tmp < x:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return right

    # def mySqrt(self, x: int) -> int:
    #     left, right = 1, x
    #     while left <= right:
    #         mid = left + right >> 1
    #         tmp = mid * mid
    #         if tmp == x:
    #             return mid
    #         elif tmp > x:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return right

    # def mySqrt(self, x):
    #     left, right = 1, x
    #     while left <= right:
    #         mid = left + right >> 1
    #         tmp = mid * mid
    #         if tmp == x:
    #             return mid
    #         elif tmp > x:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return right

    def mySqrt(self, x):
        left, right = 0, x
        while right - left > 1e-6:
            mid = (left + right) / 2
            tmp = mid * mid
            if tmp == x:
                return mid
            elif tmp > x:
                right = mid
            else:
                left = mid
        return right * 1.0


s = Solution()
a = 8
print(s.mySqrt(a))

a = 1
print(s.mySqrt(a))

a = 4
print(s.mySqrt(a))

a = 2147395599
print(s.mySqrt(a))

