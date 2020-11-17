# 求 1+2+...+n
class Solution:
    def sumNums(self, n: int) -> int:
        return n and n + self.sumNums(n-1)


s = Solution()
print(s.sumNums(3))

print(s.sumNums(9))
