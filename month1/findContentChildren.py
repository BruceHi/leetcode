# 455. 分发饼干
# 贪心
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        m, n = len(g), len(s)
        res = 0
        while i < m and j < n:
            if s[j] >= g[i]:
                res += 1
                i += 1
            j += 1
        return res


obj = Solution()
g = [1,2,3]
s = [1,1]
print(obj.findContentChildren(g, s))

g = [1, 2]
s = [1, 2, 3]
print(obj.findContentChildren(g, s))

g = [1,2]
s = []
print(obj.findContentChildren(g, s))
