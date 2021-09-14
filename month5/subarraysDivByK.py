# 和可被 K 整除的子数组
# 取模主要是用于计算机术语中。取余则更多是数学概念。两者计算结果相同。
# 使用同余定理
# 通常，涉及连续子数组问题的时候，我们使用前缀和来解决。
from typing import List
from collections import defaultdict


class Solution:
    # def subarraysDivByK(self, A: List[int], K: int) -> int:
    #     pre_mod = defaultdict(int)
    #     pre_mod[0] = 1
    #     res, total = 0, 0
    #     for num in A:
    #         total += num
    #         modulus = total % K
    #         res += pre_mod[modulus]
    #         pre_mod[modulus] += 1
    #     return res

    # def subarraysDivByK(self, A: List[int], K: int) -> int:
    #     dic = defaultdict(int)
    #     dic[0] = 1
    #     res, total = 0, 0
    #     for a in A:
    #         total += a
    #         mod = total % K
    #         res += dic[mod]
    #         dic[mod] += 1
    #     return res

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        prefix = 0
        res = 0
        for num in nums:
            prefix += num
            mod = prefix % k
            res += dic[mod]
            dic[mod] += 1
        return res


s = Solution()
A = [4,5,0,-2,-3,1]
K = 5
print(s.subarraysDivByK(A, K))
