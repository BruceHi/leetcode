#  数组中的最长山脉
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        if not n or n == 1:
            return 0
        left = float('inf')
        if A[0] < A[1]:
            left = 0
        res = 0
        for i in range(1, n-1):
            if A[i-1] > A[i] < A[i+1] or A[i-1] == A[i] < A[i+1] or A[i-1] > A[i] == A[i+1]:
                res = max(res, i - left + 1)
                left = i
        if A[-1] < A[-2]:
            res = max(res, n - left)
        return res


s = Solution()
print(s.longestMountain([2,1,4,7,3,2,5]))

print(s.longestMountain([2,2,2]))

print(s.longestMountain([]))

print(s.longestMountain([1,1,0,0,1,0]))

print(s.longestMountain([1,2,2,2]))
