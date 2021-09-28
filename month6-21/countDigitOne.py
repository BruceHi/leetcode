# 剑指 offer 43.1-n 整数中 1 出现的次数
class Solution:
    # # 超时
    # def countDigitOne(self, n: int) -> int:
    #     res = 0
    #     for i in range(1, n+1):
    #         res += str(i).count('1')
    #     return res

    # https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/
    # solution/mian-shi-ti-43-1n-zheng-shu-zhong-1-chu-xian-de-2/
    # https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/
    # solution/dong-hua-mo-ni-wo-tai-xi-huan-zhe-ge-ti-vxzwc/
    # def countDigitOne(self, n: int) -> int:
    #     digit, res = 1, 0
    #     hight, cur, low = n, 0, 0
    #     while hight or cur:
    #         cur = hight % 10
    #         hight //= 10
    #         if cur == 0:
    #             res += hight * digit
    #         elif cur == 1:
    #             res += hight * digit + low + 1
    #         else:
    #             res += (hight+1) * digit
    #         low += cur * digit
    #         digit *= 10
    #     return res

    def countDigitOne(self, n: int) -> int:
        res, digit = 0, 1
        high, low, cur = n, 0, 0
        while high or cur:
            cur = high % 10
            high //= 10
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high+1) * digit
            low += cur * digit
            digit *= 10
        return res


s = Solution()
n = 12
print(s.countDigitOne(n))

n = 13
print(s.countDigitOne(n))

n = 824883294
print(s.countDigitOne(n))

n = 101
print(s.countDigitOne(n))
