#  最长回文子串，这道题不会，操他妈
class Solution:

    # 错误
    # def longestPalindrome(self, s: str) -> str:
    #     def isPalindrom(a):
    #         return a[::-1] == a
    #
    #     length, res = 0, ''
    #     i = j = 0
    #     while j < len(s):
    #         if isPalindrom(s[i:j+1]):
    #             length += 1
    #             if length > len(res):
    #                 res = s[i:j+1]
    #             j += 1
    #         else:
    #             length = 0
    #             i = j
    #     return res

    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return len(ans)


obj = Solution()
print(obj.longestPalindrome("babad"))

print(obj.longestPalindrome("cbbd"))

print(obj.longestPalindrome("adccccbd"))