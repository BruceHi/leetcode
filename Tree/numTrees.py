# 96. 不同的二叉搜索树个数
# 卡特兰数
class Solution:
    # def numTrees(self, n: int) -> int:
    #     G = [0] * (n+1)
    #     G[0], G[1] = 1, 1
    #
    #     for i in range(2, n+1):
    #         for j in range(1, i+1):
    #             G[i] += G[j-1] * G[i-j]
    #     return G[n]

    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]


s = Solution()
print(s.numTrees(3))

print(s.numTrees(1))
