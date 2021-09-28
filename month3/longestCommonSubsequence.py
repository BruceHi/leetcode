# 1143.最长公共子序列长度
class Solution:
    # dp[i][j]：到达i, j 的最长公共子序列长度
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     m, n = len(text1), len(text2)
    #     dp = [[0] * (n+1) for _ in range(m+1)]
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if text1[i-1] == text2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1] + 1
    #             else:
    #                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #     return dp[m][n]

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     m, n = len(text1), len(text2)
    #     dp = [[0] * (n+1) for _ in range(m+1)]
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if text1[i-1] == text2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1] + 1
    #             else:
    #                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #     return dp[m][n]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]


s = Solution()
text1 = "abcde"
text2 = "ace"
print(s.longestCommonSubsequence(text1, text2))

text1 = "abc"
text2 = "abc"
print(s.longestCommonSubsequence(text1, text2))

text1 = "abc"
text2 = "def"
print(s.longestCommonSubsequence(text1, text2))

text1 = "abcde"
text2 = ""
print(s.longestCommonSubsequence(text1, text2))
