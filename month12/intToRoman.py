# 12. 整数转罗马数字
# 范围是 1-3999
# 贪心算法
class Solution:
    # def intToRoman(self, num: int) -> str:
    #     int_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    #     romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    #     res = ''
    #     for i, val in enumerate(int_list):
    #         while num >= val:
    #             res += romans[i]
    #             num -= val
    #         if not num:
    #             break
    #     return res

    def intToRoman(self, num: int) -> str:
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ''
        for i, val in enumerate(ints):
            while val <= num:
               res += romans[i]
               num -= val
            if num == 0:
                break
        return res


s = Solution()
print(s.intToRoman(3))

print(s.intToRoman(4))

print(s.intToRoman(9))

print(s.intToRoman(58))

print(s.intToRoman(1994))
