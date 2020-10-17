# 四数相加 II
from typing import List
from collections import defaultdict

class Solution:
    # 超时
    # def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    #     dic1, dic2 = defaultdict(int), defaultdict(int)
    #     for a in A:
    #         for b in B:
    #             dic1[a+b] += 1
    #     for c in C:
    #         for d in D:
    #             dic2[c+d] += 1
    #
    #     count = 0
    #     for i, v1 in dic1.items():
    #         for j, v2 in dic2.items():
    #             if not i + j:
    #                 count += v1 * v2
    #     return count

    # def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    #     dic = defaultdict(int)
    #     for a in A:
    #         for b in B:
    #             dic[a+b] += 1
    #
    #     count = 0
    #     for c in C:
    #         for d in D:
    #             count += dic[-(c+d)]
    #             # if -(c + d) in dic:
    #             #     count += dic[-(c + d)]
    #     return count

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = defaultdict(int)
        for a in A:
            for b in B:
                dic[a+b] += 1

        count = 0
        for c in C:
            for d in D:
                count += dic[-(c + d)]
        return count


s = Solution()
A = [1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(s.fourSumCount(A, B, C, D))