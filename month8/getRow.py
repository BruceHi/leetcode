# 杨辉三角 2
from typing import List


class Solution:
    # def getRow(self, rowIndex: int) -> List[int]:
    #     res = [1]
    #     for _ in range(rowIndex):
    #         res = [x+y for x, y in zip([0]+res, res+[0])]
    #     return res

    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for _ in range(rowIndex):
            res = [x + y for x, y in zip(res+[0], [0]+res)]
        return res


s = Solution()
print(s.getRow(3))

print(s.getRow(0))

print(s.getRow(1))
