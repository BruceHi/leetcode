# 521. 最长特殊序列1
from itertools import combinations


class Solution:
    # 超时
    # def findLUSlength(self, a: str, b: str) -> int:
    #
    #     def find_seq(s):
    #         res = []
    #         for i in range(len(s)):
    #             res.extend(list(map(lambda x: ''.join(x), combinations(s, i + 1))))
    #         return res
    #
    #     if len(a) < len(b):
    #         a, b = b, a
    #     seq_a, seq_b = find_seq(a), find_seq(b)
    #     for t in seq_a[::-1]:
    #         if t not in seq_b:
    #             return len(t)
    #     return -1

    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1



s = Solution()
a = "aba"
b = "cdc"
print(s.findLUSlength(a, b))

a = "aefawfawfawfaw"
b = "aefawfeawfwafwaef"
print(s.findLUSlength(a, b))
