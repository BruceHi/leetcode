# 1332. 删除回文子序列
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        return 2


obj = Solution()
s = "ababa"
print(obj.removePalindromeSub(s))

s = "abb"
print(obj.removePalindromeSub(s))

s = "baabb"
print(obj.removePalindromeSub(s))
