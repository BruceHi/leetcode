from typing import List
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        res = []
        dic = defaultdict(int)
        for i in range(len(s)-L+1):
            sub = s[i:i+L]
            dic[sub] += 1
            if dic[sub] == 2:
                res.append(sub)
        return res


obj = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(obj.findRepeatedDnaSequences(s))

s = "AAAAAAAAAAAAA"
print(obj.findRepeatedDnaSequences(s))
