# 剑指 offer 38. 字符串的排列
from typing import List
from itertools import permutations,combinations, combinations_with_replacement


class Solution:
    # def permutation(self, s: str) -> List[str]:
    #     return list(set(''.join(x) for x in permutations(s)))
    #     # return list(combinations_with_replacement(s))

    # def permutation(self, s: str) -> List[str]:
    #     return list(set(''.join(x) for x in permutations(s)))

    def permutation(self, s: str) -> List[str]:
        return list(set(''.join(x) for x in permutations(s)))

obj = Solution()
s = "abc"
print(obj.permutation(s))

s = "aab"
print(obj.permutation(s))
