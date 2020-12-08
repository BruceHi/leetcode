# 204. 计算质数
from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        for i in range(2, n+1):
            tmp = int(sqrt(i))
            j = 2
            while j <= tmp:
                if not i % j:
                    break
                j += 1
            if j == tmp + 1:
                res += 1
        return res


s = Solution()
n = 10
print(s.countPrimes(n))

n = 0
print(s.countPrimes(n))

n = 1
print(s.countPrimes(n))
