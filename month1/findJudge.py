# 997. 找到小镇的法官
from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        dic = defaultdict(list)
        in_degree = [0] * (n+1)

        for a, b in trust:
            dic[b].append(a)
            in_degree[a] += 1

        for k, v in dic.items():
            if in_degree[k] == 0:
                if len(v) == n-1:
                    return k
        return -1


s = Solution()
n = 2
trust = [[1,2]]
print(s.findJudge(n, trust))

n = 3
trust = [[1,3],[2,3]]
print(s.findJudge(n, trust))

n = 3
trust = [[1,3],[2,3],[3,1]]
print(s.findJudge(n, trust))

n = 3
trust = [[1,2],[2,3]]
print(s.findJudge(n, trust))

n = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(s.findJudge(n, trust))

n = 1
trust = []
print(s.findJudge(n, trust))  # 1

n = 2
trust = []
print(s.findJudge(n, trust))  # -1
