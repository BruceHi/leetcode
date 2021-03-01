# 409. 最长回文串
# 由这些字母所构成的回文串最长是多少（长度）
from collections import Counter


class Solution:
    # def longestPalindrome(self, s: str) -> int:
    #     res = 0
    #     count = Counter(s)
    #     for v in count.values():
    #         res += v // 2 * 2
    #         if not res & 1 and v & 1:
    #             res += 1
    #     return res

    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        flag = False
        for val in count.values():
            if val & 1:
                flag = True
                res += val - 1
            else:
                res += val
        if flag:
            res += 1
        return res


s = Solution()
print(s.longestPalindrome("abccccdd"))
