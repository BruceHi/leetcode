# 896.单调数列
from typing import List


class Solution:
    # 排序法
    # def isMonotonic(self, A: List[int]) -> bool:
    #     return A in [sorted(A), sorted(A, reverse=True)]

    # 一次遍历
    def isMonotonic(self, A: List[int]) -> bool:
        des, inc = True, True
        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                des = False
            if A[i-1] > A[i]:
                inc = False
            if not des and not inc:
                return False
        return True

s = Solution()
A = [1,2,2,3]
print(s.isMonotonic(A))

A = [6,5,4,4]
print(s.isMonotonic(A))

A = [1,3,2]
print(s.isMonotonic(A))

A = [1,2,4,5]
print(s.isMonotonic(A))

A = [1,1,1]
print(s.isMonotonic(A))
