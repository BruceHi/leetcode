# 869. 重新排序得到 2 的幂
from itertools import permutations
from math import log2


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for t in permutations(str(n)):
            if t[0] != '0':
                num = int(''.join(t))
                sqrt = log2(num)
                if int(sqrt) == sqrt:
                    return True
        return False



s = Solution()
print(s.reorderedPowerOf2(1))

print(s.reorderedPowerOf2(10))

print(s.reorderedPowerOf2(100))

print(s.reorderedPowerOf2(16))

print(s.reorderedPowerOf2(24))

print(s.reorderedPowerOf2(46))
