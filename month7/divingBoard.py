# 跳水板
from typing import List


class Solution:
    # # 超时
    # def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
    #     if not k:
    #         return []
    #     if k == 1:
    #         return [shorter, longer]
    #     res1 = list(map(lambda x: x+shorter, self.divingBoard(shorter, longer, k-1)))
    #     res2 = list(map(lambda x: x + longer, self.divingBoard(shorter, longer, k - 1)))
    #     return list(set(res1+res2))

    # 通过
    # def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
    #     if not k:
    #         return []
    #     if shorter == longer:
    #         return [shorter*k]
    #     return list(range(shorter*k, longer*k+1, longer-shorter))

    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [shorter*k]
        return list(range(shorter*k, longer*k+1, longer-shorter))


s = Solution()
shorter = 1
longer = 2
k = 3
print(s.divingBoard(shorter, longer, k))

shorter = 2
longer = 2
k = 3
print(s.divingBoard(shorter, longer, k))

shorter = 1
longer = 1
k = 0
print(s.divingBoard(shorter, longer, k))