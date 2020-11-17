# 距离顺序排列矩阵单元格
from typing import List


class Solution:
    # 直接排序，构建排序规则
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = [[i, j] for i in range(R) for j in range(C)]
        res.sort(key=lambda x: abs(x[0]-r0) + abs(x[1]-c0))
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
