# 318. 最大单词长度乘积
from typing import List


class Solution:
    # def maxProduct(self, words: List[str]) -> int:
    #     res = 0
    #     n = len(words)
    #     for i, word in enumerate(words[:-1]):
    #         for j in range(i+1, n):
    #             if not set(word) & set(words[j]):
    #                 res = max(res, len(word)*len(words[j]))
    #     return res


    def maxProduct(self, words: List[str]) -> int:
        res = 0
        n = len(words)
        mask = [0] * n
        for i, word in enumerate(words):
            for c in word:
                mask[i] |= 1 << (ord(c) - ord('a'))
        for i in range(n-1):
            for j in range(i+1, n):
                if mask[i] & mask[j] == 0:
                    res = max(res, len(words[i])*len(words[j]))
        return res



s = Solution()
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(s.maxProduct(words))

words = ["a","ab","abc","d","cd","bcd","abcd"]
print(s.maxProduct(words))

words = ["a","aa","aaa","aaaa"]
print(s.maxProduct(words))

words = ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]
print(s.maxProduct(words))
