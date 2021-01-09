# 1160. 拼写单词
from typing import List
from collections import Counter

class Solution:
    # Counter（） 非 true 也非 False，像 []，所以可以直接使用 if Counter() 判定是否为空。
    # def countCharacters(self, words: List[str], chars: str) -> int:
    #     count = Counter(chars)
    #     res = 0
    #     for word in words:
    #         if Counter(word) - count == Counter():
    #             res += len(word)
    #     return res

    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0
        for word in words:
            if not Counter(word) - count:
                res += len(word)
        return res


s = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
print(s.countCharacters(words, chars))

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(s.countCharacters(words, chars))
