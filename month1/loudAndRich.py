# 851. 喧闹和富有
# 寻找比自己有钱并且低调的人，如果没有，那么那个人就是自己。
from typing import List
from collections import defaultdict, deque


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        g = [[] for _ in range(n)]
        in_degree = [0] * len(quiet)

        # (反向)逆向拓扑图
        for a, b in richer:
            g[a].append(b)
            in_degree[b] += 1

        queue = deque([i for i, d in enumerate(in_degree) if d == 0])
        res = list(range(n))

        while queue:
            x = queue.popleft()
            for y in g[x]:
                if quiet[res[y]] > quiet[res[x]]:
                    res[y] = res[x]
                in_degree[y] -= 1
                if in_degree[y] == 0:
                    queue.append(y)
        return res


    # def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
    #     n = len(quiet)
    #     g = [[] for _ in range(n)]
    #     inDeg = [0] * n
    #     for r in richer:
    #         g[r[0]].append(r[1])
    #         inDeg[r[1]] += 1
    #
    #     ans = list(range(n))
    #     q = deque(i for i, deg in enumerate(inDeg) if deg == 0)
    #     while q:
    #         x = q.popleft()
    #         for y in g[x]:
    #             if quiet[ans[x]] < quiet[ans[y]]:
    #                 ans[y] = ans[x]  # 更新 x 的邻居的答案
    #             inDeg[y] -= 1
    #             if inDeg[y] == 0:
    #                 q.append(y)
    #     return ans



s = Solution()
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
print(s.loudAndRich(richer, quiet))

richer = []
quiet = [0]
print(s.loudAndRich(richer, quiet))
