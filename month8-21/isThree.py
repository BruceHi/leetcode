class Solution:
    def isThree(self, n: int) -> bool:
        res = 0
        for i in range(1, n+1):
            if not n % i:
                res += 1
        return res == 3


s = Solution()
n = 2
print(s.isThree(n))

n = 4
print(s.isThree(n))

print(s.isThree(5))

print(s.isThree(6))

print(sqrt(14))
print(s.isThree(14))

print(s.isThree(81))