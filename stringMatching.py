# 1408. 数组中的字符串匹配
from typing import List


class Solution:
    # def stringMatching(self, words: List[str]) -> List[str]:
    #     res = []
    #     for i, word in enumerate(words):
    #         for w in words[:i] + words[i+1:]:
    #             if word in w:
    #                 res.append(word)
    #                 break
    #     return res

    # def stringMatching(self, words: List[str]) -> List[str]:
    #     res = []
    #     for i, x in enumerate(words):
    #         for j, y in enumerate(words):
    #             if i != j and x in y:
    #                 res.append(x)
    #                 break
    #     return res

    # def stringMatching(self, words: List[str]) -> List[str]:
    #     res = []
    #     for i, x in enumerate(words):
    #         for j, y in enumerate(words):
    #             if i != j and x in y:
    #                 res.append(x)
    #                 break
    #     return res

    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i, x in enumerate(words):
            for j, y in enumerate(words):
                if i != j and x in y:
                    res.append(x)
                    break
        return res



s = Solution()
words = ["mass","as","hero","superhero"]
print(s.stringMatching(words))

words = ["leetcode","et","code"]
print(s.stringMatching(words))

words = ["blue","green","bu"]
print(s.stringMatching(words))
