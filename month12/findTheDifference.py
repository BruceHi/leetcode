# 389. 找不同
from collections import Counter


class Solution:
    # def findTheDifference(self, s: str, t: str) -> str:
    #     return list((Counter(t) - Counter(s)).elements())[0]

    # def findTheDifference(self, s: str, t: str) -> str:
    #     count = Counter(s)
    #     for c in t:
    #         if c not in count:
    #             return c
    #         count[c] -= 1
    #         if count[c] == 0:
    #             count.pop(c)

    # 位运算，异或
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for c in s:
            res ^= ord(c)
        for c in t:
            res ^= ord(c)
        return chr(res)


obj = Solution()
s = "abcd"
t = "abcde"
print(obj.findTheDifference(s, t))

s = ""
t = "y"
print(obj.findTheDifference(s, t))

s = "a"
t = "aa"
print(obj.findTheDifference(s, t))

s = "a"
t = "aa"
print(obj.findTheDifference(s, t))
