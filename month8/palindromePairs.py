# 回文对
from typing import List


class Solution:

    # # 暴力法果然超时
    # def palindromePairs(self, words: List[str]) -> List[List[int]]:
    #     res = []
    #     for idx1, word1 in enumerate(words):
    #         for idx2, word2 in enumerate(words):
    #             if word1 != word2:
    #                 tmp = word1 + word2
    #                 if tmp == tmp[::-1]:
    #                     res.append([idx1, idx2])
    #     return res

    # def palindromePairs(self, words: List[str]) -> List[List[int]]:
    #     lookup = {w: i for i, w in enumerate(words)}
    #     res = []
    #     for i, w in enumerate(words):
    #         for j in range(len(w) + 1):
    #             pre, suf = w[:j], w[j:]
                    # 判断 suf[::-1] != w 若是整体回文，只有一个匹配，那就是 ‘’
    #             if pre[::-1] == pre and suf[::-1] != w and suf[::-1] in lookup:
    #                 res.append([lookup[suf[::-1]], i])
    #             if suf[::-1] == suf and pre[::-1] != w and pre[::-1] in lookup and j != len(w):
    #                 # j != len(w)，因为 ‘’，‘w’ 与 ‘w’, ''是同一种形式，若没有最后的判断
    #                 # ‘’，‘w’ 满足一种条件，则 ‘w’，‘’ 会满足另一种条件。我们希望仅记录一次。
    #                 # 另一次，轮到另一个元素遍历记录。
    #                 res.append([i, lookup[pre[::-1]]])
    #     return res

    # #
    # def palindromePairs(self, words: List[str]) -> List[List[int]]:
    #     dic = {num: i for i, num in enumerate(words)}
    #     res = []
    #
    #     for i, word in enumerate(words):
    #         if word:
    #             for j in range(len(word)+1):
    #                 pre, suf = word[:j], word[j:]
    #                 # 刚开始判断前缀为空，整体不回文
    #                 if pre == pre[::-1] and suf[::-1] != word and suf[::-1] in dic:
    #                     res.append([dic[suf[::-1]], i])
    #                 # 开始判断整体回文，且前缀不等于当前值，即不为空
    #                 if suf == suf[::-1] and pre[::-1] in dic and j != len(word):
    #                     res.append([i, dic[pre[::-1]]])
    #
    #     return res

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic = {num: i for i, num in enumerate(words)}
        res = []

        for i, word in enumerate(words):
            if word:
                for j in range(len(word)+1):
                    pre, suf = word[:j], word[j:]
                    # 刚开始判断前缀为空，整体不回文
                    if pre == pre[::-1] and suf[::-1] != word and suf[::-1] in dic:
                        res.append([dic[suf[::-1]], i])
                    # 开始判断整体回文，且前缀不等于当前值，即不为空
                    if suf == suf[::-1] and pre[::-1] in dic and j != len(word):
                        res.append([i, dic[pre[::-1]]])

        return res


s = Solution()
print(s.palindromePairs(["abcd","dcba","lls","s","sssll"]))

print(s.palindromePairs(["bat","tab","cat"]))

print(s.palindromePairs(["aba",""]))
