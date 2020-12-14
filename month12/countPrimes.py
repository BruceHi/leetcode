# 204. 计算质数
# 统计所有小于非负整数 n 的质数的数量。
from math import sqrt


class Solution:

    # 超时，时间复杂度是 O(n sqrt(n))
    # def countPrimes(self, n: int) -> int:
    #
    #     def isprime(n):
    #         for i in range(2, int(sqrt(n))+1):
    #             if not n % i:
    #                 return False
    #         return True
    #
    #     res = 0
    #     for i in range(2, n):
    #         if isprime(i):
    #             res += 1
    #     return res

    # # 埃氏筛，质数的倍数被称为合数（不包括该质数本身）
    # def countPrimes(self, n: int) -> int:
    #     prime = [1] * n
    #     res = 0
    #     for i in range(2, n):
    #         if prime[i]:
    #             res += 1
    #             for j in range(i*i, n, i):
    #                 prime[j] = 0
    #     return res

    # # 线性筛
    # 时间复杂度为 O(n)
    def countPrimes(self, n: int) -> int:
        primes = []
        flag = [1] * n
        for i in range(2, n):
            if flag[i]:
                primes.append(i)
            for j in primes:
                if i * j >= n:
                    break
                flag[i*j] = 0
                if not i % j:  # 保证每一个合数，仅被自身的第一个质因数筛除
                    break
        return len(primes)


s = Solution()
n = 10
print(s.countPrimes(n))

n = 0
print(s.countPrimes(n))

n = 1
print(s.countPrimes(n))

n = 2
print(s.countPrimes(n))
