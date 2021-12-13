# 166. 分数到小数
class Solution:
    # 官方题解
    # 看不懂先调试模拟一下，然后再看文字。
    # def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    #     if numerator % denominator == 0:
    #         return str(numerator // denominator)
    #
    #     s = []
    #     if (numerator < 0) != (denominator < 0):
    #         s.append('-')
    #
    #     # 整数部分
    #     numerator = abs(numerator)
    #     denominator = abs(denominator)
    #     integerPart = numerator // denominator
    #     s.append(str(integerPart))
    #     s.append('.')
    #
    #     # 小数部分
    #     indexMap = {}
    #     remainder = numerator % denominator
    #     while remainder and remainder not in indexMap:
    #         indexMap[remainder] = len(s)
    #         remainder *= 10
    #         s.append(str(remainder // denominator))
    #         remainder %= denominator
    #     if remainder:  # 有循环节
    #         insertIndex = indexMap[remainder]
    #         s.insert(insertIndex, '(')
    #         s.append(')')
    #
    #     return ''.join(s)

    # def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    #     if numerator % denominator == 0:
    #         return str(numerator//denominator)
    #
    #     res = []
    #     if numerator * denominator < 0:
    #         res.append('-')
    #
    #     a, b = abs(numerator), abs(denominator)
    #     res.append(str(a // b))
    #     res.append('.')
    #
    #     dic = {}
    #     remain = a % b
    #     while remain and remain not in dic:
    #         dic[remain] = len(res)
    #         remain *= 10
    #         res.append(str(remain // b))
    #         remain %= b
    #
    #     if remain:
    #         i = dic[remain]
    #         res.insert(i, '(')
    #         res.append(')')
    #
    #     return ''.join(res)

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        res = []
        if numerator * denominator < 0:
            res.append('-')

        a, b = abs(numerator), abs(denominator)
        res.append(str(a//b))
        res.append('.')

        remain = a % b
        dic = {}
        while remain and remain not in dic:
            dic[remain] = len(res)
            remain *= 10
            res.append(str(remain//b))
            remain %= b
        if remain:
            res.insert(dic[remain], '(')
            res.append(')')

        return ''.join(res)


s = Solution()
numerator = 1
denominator = 2
print(s.fractionToDecimal(numerator, denominator))

numerator = 2
denominator = 1
print(s.fractionToDecimal(numerator, denominator))

numerator = 2
denominator = 3
print(s.fractionToDecimal(numerator, denominator))

numerator = 4
denominator = 333
print(s.fractionToDecimal(numerator, denominator))

numerator = 1
denominator = 5
print(s.fractionToDecimal(numerator, denominator))
