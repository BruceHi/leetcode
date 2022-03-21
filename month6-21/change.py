# 518. 零钱兑换 2
from typing import List


class Solution:
    # 错误，没有去除重复的，得到的是排列数，比如 (1, 2) 与 （2, 1）其实是一种情况
    # 但在这里也统计了。
    # def change(self, amount: int, coins: List[int]) -> int:
    #     dp = [0] * (amount+1)
    #     dp[0] = 1
    #     for i in range(1, amount+1):
    #         for coin in coins:
    #             if i - coin >= 0:
    #                 dp[i] += dp[i-coin]
    #     return dp[amount]

    # 每一次for coin in coins循环中就把coin的可使用次数规定好了。
    # 不允许在后面的硬币层次使用之前的硬币。
    # 这就像排列中2,2,1; 2,1,2是两种情况，但是组合问题规定好了一种书写顺序，比如大的写在前面那就只有2,2,1这一种情况了。
    # def change(self, amount: int, coins: List[int]) -> int:
    #     dp = [0] * (amount + 1)
    #     dp[0] = 1
    #
    #     # 这种是组合问题，
    #     for coin in coins:
    #         for x in range(coin, amount + 1):
    #             dp[x] += dp[x - coin]
    #     return dp[amount]

    # def change(self, amount: int, coins: List[int]) -> int:
    #     dp = [0] * (amount+1)
    #     dp[0] = 1
    #     for coin in coins:
    #         for x in range(coin, amount+1):
    #             dp[x] += dp[x-coin]
    #     return dp[amount]

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]


s = Solution()
amount = 5
coins = [1, 2, 5]
print(s.change(amount, coins))

amount = 3
coins = [2]
print(s.change(amount, coins))

amount = 10
coins = [10]
print(s.change(amount, coins))
