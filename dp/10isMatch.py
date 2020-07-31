# 通配符匹配
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] | dp[i][j-1]
        return dp[m][n]


obj = Solution()
s = "aa"
p = "a"
print(obj.isMatch(s, p))

s = "aa"
p = "*"
print(obj.isMatch(s, p))

s = "cb"
p = "?a"
print(obj.isMatch(s, p))

s = "adceb"
p = "*a*b"
print(obj.isMatch(s, p))

s = "acdcb"
p = "a*c?b"
print(obj.isMatch(s, p))