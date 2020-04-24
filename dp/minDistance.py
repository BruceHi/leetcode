# 最小编辑距离
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2+1) for _ in range(len1+1)]  # 注意 len1 * len2 的矩阵，其中 len1 在后面位置

        # 二维动态规划的初始值都是一行一列
        for i in range(len1+1):
            dp[i][0] = i
        for j in range(len2+1):
            dp[0][j] = j

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                # flag = 0 if word1[i-1] == word2[j-1] else 1  # 代表的是第 i 个单词和第 j 个单词。
                # dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+flag)
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[len1][len2]


s = Solution()
word1 = "horse"
word2 = "ros"
print(s.minDistance(word1, word2))

word1 = "intention"
word2 = "execution"
print(s.minDistance(word1, word2))

word1 = "big"
word2 = "bic"
print(s.minDistance(word1, word2))
