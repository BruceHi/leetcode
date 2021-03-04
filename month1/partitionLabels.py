# 763. 划分字母区间
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {}
        for i, c in enumerate(S):
            dic[c] = i

        res = []
        start = end = 0
        for i, c in enumerate(S):
            end = max(end, dic[c])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res


obj = Solution()
S = "ababcbacadefegdehijhklij"
print(obj.partitionLabels(S))
