# 正则表达式匹配
import re


class Solution:
    # def isMatch(self, s: str, p: str) -> bool:
    #     pattern = re.compile('^' + p + '$')
    #     res = pattern.match(s)
    #     if res:
    #         return True
    #     return False

    # 动态规划
    # def isMatch(self, s: str, p: str) -> bool:
    #     m, n = len(s), len(p)
    #     dp = [[False] * (n+1) for _ in range(m+1)]
    #     dp[0][0] = True
    #
    #     for j in range(2, n+1):
    #         if p[j-1] == '*':  # 从 1 开始也没毛病，毕竟 p[0] 不可能等于 *
    #             dp[0][j] = dp[0][j-2]
    #         # else:  # 不能直接赋值为 true,再退出,因为后面可能会再遇见 *。
    #         #     break
    #
    #     # Python 中没考虑下标越界的情况，是因为默认正则表达式必须是正确的，而不是错误的。
    #     # 比如 `*a`，就是个错误的表达式。
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if p[j-1] == '.' or p[j-1] == s[i-1]:
    #                 dp[i][j] = dp[i-1][j-1]
    #             elif p[j-1] == '*':  # 去掉 j > 1 判断也行，毕竟 p[0] 不可能等于 * ，否则就是错误的正则表达式。
    #                 if p[j-2] == s[i-1] or p[j-2] == '.':
    #                     dp[i][j] = dp[i][j-2] | dp[i-1][j]
    #                 else:
    #                     dp[i][j] = dp[i][j-2]
    #     return dp[m][n]

    # def isMatch(self, s: str, p: str) -> bool:
    #     pattern = re.compile('^' + p + '$')
    #     if pattern.findall(s):
    #         return True
    #     return False

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '.' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]

        return dp[m][n]




obj = Solution()
s = "aab"
p = "c*a*b"
print(obj.isMatch(s, p))


s = "aa"
p = "a"
print(obj.isMatch(s, p))

s = "aa"
p = "a*"
print(obj.isMatch(s, p))

obj = Solution()
s = "ab"
p = ".*"
print(obj.isMatch(s, p))

s = "mississippi"
p = "mis*is*p*."
print(obj.isMatch(s, p))

# .* 两个连在一起是匹配任何字符的
s = "a"
p = ".*"
print(obj.isMatch(s, p))

s = "a"
p = "ab*a"
print(obj.isMatch(s, p))

s = "a"
p = "ab*a"
print(obj.isMatch(s, p))
