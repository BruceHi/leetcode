# 516. 最长回文子序列的长度
class Solution:
    # 从中心扩展
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # dp(i, j):索引从i到j 的最长回文子序列长度为dp
        # 注意 i 要从右到左，因为结果是求 dp[0][n-1]
        # j 是从左到右 正常顺序
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        print(dp)
        return dp[0][n-1]


obj = Solution()
s = "bbbab"
print(obj.longestPalindromeSubseq(s))

s = "cbbd"
print(obj.longestPalindromeSubseq(s))
