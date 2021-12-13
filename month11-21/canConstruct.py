# 383. 赎金信
from collections import Counter


class Solution:
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     return Counter(ransomNote) - Counter(magazine) == Counter()

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)


s = Solution()
ransomNote = "a"
magazine = "b"
print(s.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "ab"
print(s.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "aab"
print(s.canConstruct(ransomNote, magazine))
