# 1071. 字符串的最大公因子
from collections import Counter
from math import gcd


class Solution:
    # 失败
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    #     count1, count2 = Counter(str1), Counter(str2)
    #     if count1.keys() == count2.keys():
    #         return ''.join(count1.keys())
    #     return ''

    # 数学方法
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            gcd_len = gcd(len(str1), len(str2))
            return str1[:gcd_len]
        return ''


s = Solution()
str1 = "ABCABC"
str2 = "ABC"
print(s.gcdOfStrings(str1, str2))

str1 = "ABABAB"
str2 = "ABAB"
print(s.gcdOfStrings(str1, str2))

str1 = "LEET"
str2 = "CODE"
print(s.gcdOfStrings(str1, str2))


str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
print(s.gcdOfStrings(str1, str2))
