# 500. 键盘行
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('qwertyuiop')
        set1.update('qwertyuiop'.upper())
        set2 = set('asdfghjkl')
        set2.update('asdfghjkl'.upper())
        set3 = set('zxcvbnm')
        set3.update('zxcvbnm'.upper())
        res = []
        for word in words:
            tmp = set(word)
            if tmp.issubset(set1) or tmp.issubset(set2) or tmp.issubset(set3):
                res.append(word)
        return res


s = Solution()
words = ["Hello","Alaska","Dad","Peace"]
print(s.findWords(words))

words = ["omk"]
print(s.findWords(words))

words = ["adsdf","sfd"]
print(s.findWords(words))

# a = 'abc'
# print(a.upper())
