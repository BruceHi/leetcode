# 1446. 连续字符
class Solution:
    def maxPower(self, s: str) -> int:
        res, i = 0, 0
        for j, c in enumerate(s):
            if c != s[i]:
                res = max(res, j-i)
                i = j
        if s[-1] == s[i]:
            res = max(res, len(s)-i)
        return res

obj = Solution()
s = "leetcode"
print(obj.maxPower(s))

s = "abbcccddddeeeeedcba"
print(obj.maxPower(s))

s = "triplepillooooow"
print(obj.maxPower(s))

s = "hooraaaaaaaaaaay"
print(obj.maxPower(s))

s = "hooraaaaaaaaaaa"
print(obj.maxPower(s))

s = "tourist"
print(obj.maxPower(s))

s = "t"
print(obj.maxPower(s))