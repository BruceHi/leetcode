# 12. 整数转罗马数字
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
               4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        res = ''
        while num:



s = Solution()
print(s.intToRoman(3))

print(s.intToRoman(4))

print(s.intToRoman(9))

print(s.intToRoman(58))

print(s.intToRoman(1994))

