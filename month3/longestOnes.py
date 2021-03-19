# 1004.最大连续 1 的个数 3
# 滑动窗口
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        res = 0
        left, right = 0, 0
        zeros = 0
        while right < n:
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res



s = Solution()
A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
print(s.longestOnes(A, K))

A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(s.longestOnes(A, K))
