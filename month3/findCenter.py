# 1791. 找出星型图的中心节点
from typing import List
from collections import defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = defaultdict(int)
        for a, b in edges:
            dic[a] += 1
            dic[b] += 1
            if dic[a] >= 2:
                return a
            if dic[b] >= 2:
                return b

s = Solution()
edges = [[1,2],[2,3],[4,2]]
print(s.findCenter(edges))

edges = [[1,2],[5,1],[1,3],[1,4]]
print(s.findCenter(edges))
