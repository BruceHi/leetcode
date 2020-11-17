#  数组中的最长山脉
from typing import List


class Solution:
    # # 失败，遇见 最高处相等，2, 3, 3, 2, 0, 2 就不行。
    # def longestMountain(self, A: List[int]) -> int:
    #     n = len(A)
    #     if not n or n == 1:
    #         return 0
    #     left = float('inf')
    #     if A[0] < A[1]:
    #         left = 0
    #     res = 0
    #     for i in range(1, n-1):
    #         if A[i-1] > A[i] < A[i+1]:
    #             res = max(res, i - left + 1)
    #             left = i
    #         elif A[i-1] == A[i]:
    #             left = i
    #         elif A[i] == A[i+1]:
    #             left = i + 1
    #     if A[-1] < A[-2]:
    #         res = max(res, n - left)
    #     return res

    # 开头和末尾无法做为山顶，但可以做为山脚。
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        left = [0] * n
        for i in range(1, n):
            if A[i-1] < A[i]:
                left[i] = left[i-1] + 1

        right = [0] * n
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]:
                right[i] = right[i+1] + 1

        res = 0
        for i in range(n):
            if left[i] and right[i]:
                res = max(res, left[i] + right[i] + 1)  # 末尾莫忘加 1.
        return res



s = Solution()
print(s.longestMountain([2,1,4,7,3,2,5]))

print(s.longestMountain([2,2,2]))

print(s.longestMountain([]))

print(s.longestMountain([1,1,0,0,1,0]))

print(s.longestMountain([1,2,2,2]))

print(s.longestMountain([2, 0, 2, 2, 3]))

print(s.longestMountain([2, 3, 3, 2, 0, 2]))
