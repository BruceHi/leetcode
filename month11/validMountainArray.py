# 有效的山脉数组
from typing import List


class Solution:
    # def validMountainArray(self, A: List[int]) -> bool:
    #     if not A:
    #         return False
    #     top = max(A)
    #     idx = A.index(top)
    #     if not idx or idx == len(A) - 1:
    #         return False
    #
    #     for i in range(idx):
    #         if A[i] >= A[i+1]:
    #             return False
    #     for i in range(idx, len(A)-1):
    #         if A[i] <= A[i+1]:
    #             return False
    #     return True


    def validMountainArray(self, A: List[int]) -> bool:
        i = 0
        n = len(A)

        while i < n-1 and A[i] < A[i+1]:
            i += 1

        if not i or i == n - 1:
            return False

        while i < n-1 and A[i] > A[i+1]:
            i += 1

        return i == n - 1


s = Solution()
print(s.validMountainArray([]))

print(s.validMountainArray([2]))

print(s.validMountainArray([2, 1]))

print(s.validMountainArray([3, 5, 5]))

print(s.validMountainArray([0, 3, 2, 1]))
