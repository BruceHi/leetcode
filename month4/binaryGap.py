# 868. 二进制间距
class Solution:
    # def binaryGap(self, n: int) -> int:
    #     if n & (n - 1) == 0:
    #         return 0
    #     nums = bin(n)
    #     a = 0
    #     res = 0
    #     for i, c in enumerate(nums[2:]):
    #         if c == '1':
    #             res = max(res, i - a)
    #             a = i
    #     return res


    # 使用移位，从后往前开始
    # def binaryGap(self, n: int) -> int:
    #     last, res, i = -1, 0, 0
    #     while n:
    #         if n & 1:
    #             if last != -1:
    #                 res = max(res, i - last)
    #             last = i
    #         n >>= 1
    #         i += 1
    #     return res

    def binaryGap(self, n: int) -> int:
        res = 0
        last = -1
        i = 0
        while n:
            if n & 1:
                if last != -1:
                    res = max(res, i-last)
                last = i
            n >>= 1
            i += 1
        return res


s = Solution()
n = 22
print(s.binaryGap(n))

n = 8
print(s.binaryGap(n))

n = 5
print(s.binaryGap(n))
