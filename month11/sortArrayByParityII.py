# 按奇偶排序数组二
from typing import List


class Solution:
    # def sortArrayByParityII(self, A: List[int]) -> List[int]:
    #     if not A:
    #         return []
    #     n = len(A)
    #     res = [0] * n
    #     i, j = 0, 1
    #     for a in A:
    #         if a & 1:
    #             res[j] = a
    #             j += 2
    #         else:
    #             res[i] = a
    #             i += 2
    #     return res

    # 原地修改
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        j = 1
        for i in range(0, n, 2):
            if A[i] & 1:
                while A[j] & 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


s = Solution()
print(s.sortArrayByParityII([4,2,5,7]))

print(s.sortArrayByParityII([2, 3]))
