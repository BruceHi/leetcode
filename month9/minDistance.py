# 583. 两个字符串的删除操作
# 使得两个字符串长度相同的最少操作步骤
class Solution:
    # dp[i][j]：到达i, j 的最长公共子序列长度
    # 1. 求出最长公共子序列的长度，然后再减去
    # def minDistance(self, word1: str, word2: str) -> int:
    #     m, n = len(word1), len(word2)
    #     dp = [[0] * (n+1) for _ in range(m+1)]
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if word1[i-1] == word2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1] + 1
    #             else:
    #                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #
    #     return m + n - dp[m][n] * 2

    # 其中 dp[i][j] 表示使 word1[0:i] 和 word2[0:j] 相同的最少删除操作次数。
    # 与 最小编辑距离 相似
    # def minDistance(self, word1: str, word2: str) -> int:
    #     m, n = len(word1), len(word2)
    #     dp = [[0] * (n+1) for _ in range(m+1)]
    #
    #     # 初始化
    #     for i in range(1, m+1):
    #         dp[i][0] = i
    #     for j in range(1, n+1):
    #         dp[0][j] = j
    #
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if word1[i-1] == word2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1]
    #             else:
    #                 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
    #     return dp[m][n]

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[m][n]


s = Solution()
word1, word2 = "sea", "eat"
print(s.minDistance(word1, word2))

word1 = "leetcode"
word2 = "etco"
print(s.minDistance(word1, word2))
