# 299. 猜数字游戏
from collections import Counter


class Solution:
    # def getHint(self, secret: str, guess: str) -> str:
    #     countA = 0
    #     for a, b in zip(secret, guess):
    #         if a == b:
    #             countA += 1
    #     count1, count2 = Counter(secret), Counter(guess)
    #     count = count1 & count2
    #     return str(countA) + 'A' + str(sum(count.values())-countA) + 'B'

    def getHint(self, secret: str, guess: str) -> str:
        countA = 0
        s, g = [0] * 10, [0] * 10
        for a, b in zip(secret, guess):
            if a == b:
                countA += 1
            else:
                s[int(a)] += 1
                g[int(b)] += 1
        countB = sum(min(a, b) for a, b in zip(s, g))
        return f'{countA}A{countB}B'

s = Solution()
secret = "1807"
guess = "7810"
print(s.getHint(secret, guess))

secret = "1123"
guess = "0111"
print(s.getHint(secret, guess))

secret = "1"
guess = "0"
print(s.getHint(secret, guess))

secret = "1"
guess = "1"
print(s.getHint(secret, guess))