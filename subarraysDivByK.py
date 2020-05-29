# 和可被 K 整除的子数组
from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        pre_mod = defaultdict(int)
        pre_mod[0] = 1
        res, total = 0, 0
        for num in A:
            total += num
            modulus = total % K
            res += pre_mod[modulus]
            pre_mod[modulus] += 1
        return res


s = Solution()
A = [4,5,0,-2,-3,1]
K = 5
print(s.subarraysDivByK(A, K))

A = [4,5,0,-2,-3,1]
K = 5
print(s.subarraysDivByK(A, K))
