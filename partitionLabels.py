# 763. 划分字母区间
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        i = 0
        res = []
        while i < n:


obj = Solution()
S = "ababcbacadefegdehijhklij"
print(obj.partitionLabels(S))
