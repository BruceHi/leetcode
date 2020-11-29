# 171.Excel 表列序号
from string import ascii_uppercase


class Solution:
    # def titleToNumber(self, s: str) -> int:
    #     # 不能写成 a in ascii_uppercase b in range(1, 27)，这样就是全排列了
    #     dic = {a: b for a, b in zip(ascii_uppercase, range(1, 27))}
    #     res = 0
    #     for c in s:
    #         res *= 26
    #         res += dic[c]
    #     return res

    def titleToNumber(self, s: str) -> int:
        base = ord('A')
        res = 0
        for c in s:
            res *= 26
            res += ord(c) - base + 1
        return res

s = Solution()
print(s.titleToNumber('A'))

print(s.titleToNumber('AB'))

print(s.titleToNumber('ZY'))
