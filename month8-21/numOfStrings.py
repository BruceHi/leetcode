from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for p in patterns:
            if p in word:
                res += 1
        return res


s = Solution()
patterns = ["a","abc","bc","d"]
word = "abc"
print(s.numOfStrings(patterns, word))

patterns = ["a","b","c"]
word = "aaaaabbbbb"
print(s.numOfStrings(patterns, word))

patterns = ["a","a","a"]
word = "ab"
print(s.numOfStrings(patterns, word))