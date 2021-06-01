# 零钱找零：给定不同的硬币（可用多次或不用）进行找零，求最小需要几枚
from typing import List


class Solution:
    # def coinChange(self, coins, amount) -> int:
    #
    #     dp = [float('inf')] * (amount+1)
    #     dp[0] = 0
    #
    #     for i in range(amount+1):
    #         for coin in coins:
    #             if coin <= i:
    #                 dp[i] = min(dp[i-coin]+1, dp[i])
    #
    #     return dp[amount] if dp[amount] != float('inf') else -1

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     dp = [float('inf')] * (amount+1)
    #     dp[0] = 0
    #     for i in range(1, amount+1):
    #         for coin in coins:
    #             if i - coin >= 0:
    #                 dp[i] = min(dp[i-coin] + 1, dp[i])
    #     return dp[amount] if dp[amount] != float('inf') else -1

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     dp = [float('inf')] * (amount+1)
    #     dp[0] = 0
    #
    #     for coin in coins:
    #         for x in range(coin, amount+1):  # 少了许多判断
    #             dp[x] = min(dp[x-coin] + 1, dp[x])
    #     return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1



s = Solution()
coins = [1, 2, 5]
amount = 11
print(s.coinChange(coins, amount))

coins = [2]
amount = 3
print(s.coinChange(coins, amount))

coins = [1]
amount = 0
print(s.coinChange(coins, amount))

coins = [1]
amount = 1
print(s.coinChange(coins, amount))

coins = [1]
amount = 2
print(s.coinChange(coins, amount))

# 贪心法 反例
coins = [4, 5]
amount = 16
print(s.coinChange(coins, amount))