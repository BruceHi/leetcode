# 717. 1比特与2比特字符
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)
        while i < n-1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return True if i < n else False


s = Solution()
bits = [1, 0, 0]
print(s.isOneBitCharacter(bits))

bits = [1, 1, 1, 0]
print(s.isOneBitCharacter(bits))
