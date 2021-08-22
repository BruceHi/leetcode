from typing import List


class Solution:
    # def isPrefixString(self, s: str, words: List[str]) -> bool:
    #     return ''.join(words).startswith(s)

    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for word in words:
            n = len(word)
            if s[i:n+i] != word:
                return False
            i += n
            if i == len(s):
                return True
        return False



obj = Solution()
s = "iloveleetcode"
words = ["i","love","leetcode","apples"]
print(obj.isPrefixString(s, words))

s = "iloveleetcode"
words = ["apples","i","love","leetcode"]
print(obj.isPrefixString(s, words))

s = "a"
words = ["aa","i","love","leetcode"]
print(obj.isPrefixString(s, words))

s = "ccccccccc"
words = ["c","cc"]
print(obj.isPrefixString(s, words))

