# 面试题 01.04.回文排列
from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        count = 0
        for val in counter.values():
            if val & 1:
                count += 1
            if count > 1:
                return False
        return True


obj = Solution()
s = "tactcoa"
print(obj.canPermutePalindrome(s))
