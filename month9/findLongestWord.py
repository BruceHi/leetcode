# 524. 通过删除字母匹配到字典里最长的单词
from typing import List


class Solution:
    # def findLongestWord(self, s: str, dictionary: List[str]) -> str:
    #     def isWord(s, t):
    #         i = 0
    #         for c in s:
    #             if t[i] == c:
    #                 i += 1
    #                 if i == len(t):
    #                     return True
    #         return False
    #
    #     res = []
    #     for d in dictionary:
    #         if isWord(s, d):
    #             res.append(d)
    #
    #     if not res:
    #         return ''
    #     res.sort(key=lambda x: (-len(x), x))
    #     return res[0]

    # 先排序，然后返回第一个匹配到的。
    # def findLongestWord(self, s: str, dictionary: List[str]) -> str:
    #     dictionary.sort(key=lambda x: (-len(x), x))
    #
    #     for d in dictionary:
    #         i, j = 0, 0
    #         while i < len(d) and j < len(s):
    #             if d[i] == s[j]:
    #                 i += 1
    #             j += 1
    #         if i == len(d):
    #             return d
    #     return ''

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))

        for d in dictionary:
            i = 0
            for c in s:
                if d[i] == c:
                    i += 1
                    if i == len(d):
                        return d
        return ''


obj = Solution()
s = "abpcplea"
dictionary = ["ale","apple","monkey","plea", "abple"]
print(obj.findLongestWord(s, dictionary))

s = "abpcplea"
dictionary = ["a","b","c"]
print(obj.findLongestWord(s, dictionary))
