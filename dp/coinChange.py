# 零钱找零：给定不同的硬币（可用多次或不用）进行找零，求最小需要几枚
class Solution:
    def coinChange(self, coins, amount) -> int:

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i-coin]+1, dp[i])

        return dp[amount] if dp[amount] != float('inf') else -1


s = Solution()
coins = [1, 2, 5]
amount = 11
print(s.coinChange(coins, amount))

coins = [2]
amount = 3
print(s.coinChange(coins, amount))
