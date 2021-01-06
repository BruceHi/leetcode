# 1160. 拼写单词
from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0
        for word in words:
            if Counter(word) - count == Counter():
                res += len(word)
        return res


s = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
print(s.countCharacters(words, chars))

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(s.countCharacters(words, chars))
