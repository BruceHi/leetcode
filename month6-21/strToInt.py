# 剑指 offer 67. 把字符串转换为整数
import re


class Solution:
    def strToInt(self, str) -> int:
        p = r'^\s*[+-]?\d+'
        pattern = re.compile(p)
        res = pattern.match(str)
        if res:
            res = int(res.group())
            if res < -2**31:
                return -2**31
            if res > 2**31-1:
                return 2**31-1
            return res
        else:
            return 0


s = Solution()
str = "42"
print(s.strToInt(str))

str = "   -42"
print(s.strToInt(str))

str = "4193 with words"
print(s.strToInt(str))

str = "words and 987"
print(s.strToInt(str))

str = "-91283472332"
print(s.strToInt(str))

# print(int(' -123'))
