# 距离顺序排列矩阵单元格
from typing import List
from collections import defaultdict


class Solution:
    # # 直接排序，构建排序规则，时间复杂度 RClog(RC)
    # def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    #     res = [[i, j] for i in range(R) for j in range(C)]  # 注意这种两个 for 的写法
    #     res.sort(key=lambda x: abs(x[0]-r0) + abs(x[1]-c0))
    #     return res

    # 桶排序，实际上只用到了分桶，因为不要求相同的顺序
    # 时间复杂度：O(RC)，空间复杂度：O(RC)
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        max_dist = max(r0, abs(R - 1 - r0)) + max(c0, abs(C - 1 - c0))
        buck = defaultdict(list)
        dist = lambda r1, r2, c1, c2: abs(r1 - r2) + abs(c1 - c2)

        for i in range(R):
            for j in range(C):
                buck[dist(i, r0, j, c0)].append([i, j])

        res = []
        for i in range(max_dist+1):
            res.extend(buck[i])
        return res


s = Solution()
R = 1
C = 2
r0 = 0
c0 = 0
print(s.allCellsDistOrder(R, C, r0, c0))

R = 2
C = 2
r0 = 0
c0 = 1
print(s.allCellsDistOrder(R, C, r0, c0))

R = 2
C = 3
r0 = 1
c0 = 2
print(s.allCellsDistOrder(R, C, r0, c0))
