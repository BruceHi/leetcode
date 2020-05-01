# 不使用运算符 + 和 -，计算两整数​a、b 之和。
# https://leetcode-cn.com/problems/sum-of-two-integers/solution/python-wei-yun-suan-yi-xie-keng-by-lih/
class Solution:
    # 其他语言描述，自动判别溢出
    # def getSum(self, a: int, b: int) -> int:
    #     while b:
    #         a, b = a ^ b, (a & b) << 1
    #     return a

    #  python整数类型为 Unifying Long Integers，需要模拟 32 位内存。
    def getSum(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            a, b = a ^ b, ((a & b) << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)


s = Solution()
a = 1
b = 2
print(s.getSum(a, b))

s = Solution()
a = -2
b = 3
print(s.getSum(a, b))
