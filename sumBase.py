class Solution:
    def sumBase(self, n: int, k: int) -> int:

        def convertToBase(num, base):
            if num < base:
                return str(num)
            return convertToBase(num // base, base) + str(num % base)

        n = int(convertToBase(n, k))
        res = 0
        while n:
            res += n % 10
            n //= 10
        return res



s = Solution()
n = 34
k = 6
print(s.sumBase(n, k))

n = 10
k = 10
print(s.sumBase(n, k))
