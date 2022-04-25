# 806. 写字符串需要的行数
from typing import List


class Solution:
    # def numberOfLines(self, widths: List[int], s: str) -> List[int]:
    #     row = 1
    #     count = 0
    #     for c in s:
    #         v = widths[ord(c)-ord('a')]
    #         if count + v <= 100:
    #             count += v
    #         else:
    #             count = v
    #             row += 1
    #     return [row, count]

    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line, remain = 1, 0
        for c in s:
            length = widths[ord(c) - ord('a')]
            remain += length
            if remain > 100:
                line += 1
                remain = length
        return [line, remain]


s = Solution()
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
print(s.numberOfLines(widths, S))

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
print(s.numberOfLines(widths, S))
