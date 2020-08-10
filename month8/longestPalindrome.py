#  最长回文子串，这道题不会，操他妈
class Solution:

    # 错误
    def longestPalindrome(self, s: str) -> str:
        def isPalindrom(a):
            return a[::-1] == a

        length, res = 0, ''
        i = j = 0
        while j < len(s):
            if isPalindrom(s[i:j+1]):
                length += 1
                if length > len(res):
                    res = s[i:j+1]
                j += 1
            else:
                length = 0
                i = j
        return res


obj = Solution()
print(obj.longestPalindrome("babad"))

print(obj.longestPalindrome("cbbd"))