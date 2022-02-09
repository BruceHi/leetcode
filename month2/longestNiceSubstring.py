# 1763. 最长的美好子字符串
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def niceSub(s):
            s = set(s)
            for c in s:
                if c.isupper():
                    if c.lower() not in s:
                        return False
                else:
                    if c.upper() not in s:
                        return False
            return True



obj = Solution()
s = "YazaAay"
s.lower()
print(obj.longestNiceSubstring(s))

s = "Bb"
print(obj.longestNiceSubstring(s))

s = "c"
print(obj.longestNiceSubstring(s))

s = "dDzeE"
print(obj.longestNiceSubstring(s))
