# 最佳观光组合
# https://leetcode-cn.com/problems/best-sightseeing-pair/solution/python-jie-fa-by-jiayangwu/
from typing import List

class Solution:
    # def maxScoreSightseeingPair(self, A: List[int]) -> int:
    #     n = len(A)
    #     res = float('-inf')
    #     for i, num in enumerate(A[:-1]):
    #         for j in range(i+1, n):
    #             tmp = num + A[j] + i - j
    #             if tmp > res:
    #                 res = tmp
    #     return res

    # def maxScoreSightseeingPair(self, A: List[int]) -> int:
    #     res = 0
    #     pre_max = A[0]
    #     for j in range(1, len(A)):  # 使用enumerate 前面变了，会改变索引位置
    #         res = max(res, pre_max + A[j] - j)
    #         pre_max = max(pre_max, A[j] + j)
    #     return res

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        pre_max = A[0]
        for i in range(1, len(A)):
            res = max(res, pre_max + A[i] - i)
            pre_max = max(pre_max, A[i] + i)  # 注意这是个加号。
        return res


s = Solution()
nums = [8,1,5,2,6]
print(s.maxScoreSightseeingPair(nums))

nums = [1,3,5]
print(s.maxScoreSightseeingPair(nums))
