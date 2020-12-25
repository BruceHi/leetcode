# 最长回文串
# 由这些字母所构成的回文串最长是多少
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        count = Counter(s)
        for v in count.values():
            res += v // 2 * 2
            if not res & 1 and v & 1:
                res += 1
        return res


s = Solution()
print(s.longestPalindrome("abccccdd"))
