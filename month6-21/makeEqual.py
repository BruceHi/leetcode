from typing import List
from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        res = ''
        for word in words:
            for c in word:
                res += c
        count = Counter(res)
        for v in count.values():
            if v % len(words) != 0:
                return False
        return True


s = Solution()
words = ["abc","aabc","bc"]
print(s.makeEqual(words))

words = ["ab","a"]
print(s.makeEqual(words))

words = ['b']
print(s.makeEqual(words))
