# 单词拆分，所有拆分结果必须都在字典列表中
from typing import List


class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     n = len(s)
    #     dp = [True] + [False] * n
    #     words = set(wordDict)
    #     for i in range(1, n+1):
    #         for j in range(i):
    #             if dp[j] and s[j:i] in words:
    #                 dp[i] = True
    #                 break
    #     return dp[n]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        words = set(wordDict)
        for i in range(1, n+1):
            for j in range(i):
                dp[i] = dp[j] and s[j:i] in words
                if dp[i]:
                    break
        return dp[n]




obj = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print(obj.wordBreak(s, wordDict))

s = "applepenapple"
wordDict = ["apple", "pen"]
print(obj.wordBreak(s, wordDict))

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(obj.wordBreak(s, wordDict))

s = "a"
wordDict = []
print(obj.wordBreak(s, wordDict))

s = "bb"
wordDict = ["a","b","bbb","bbbb"]
print(obj.wordBreak(s, wordDict))

s = "cars"
wordDict = ["car","ca","rs"]
print(obj.wordBreak(s, wordDict))