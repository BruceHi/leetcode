# 正则表达式匹配
import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.compile('^' + p + '$')
        res = pattern.match(s)
        if res:
            return True
        return False


obj = Solution()
s = "aa"
p = "a"
print(obj.isMatch(s, p))

obj = Solution()
s = "aa"
p = "a*"
print(obj.isMatch(s, p))

obj = Solution()
s = "ab"
p = ".*"
print(obj.isMatch(s, p))

obj = Solution()
s = "aab"
p = "c*a*b"
print(obj.isMatch(s, p))

obj = Solution()
s = "mississippi"
p = "mis*is*p*."
print(obj.isMatch(s, p))

