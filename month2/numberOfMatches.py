# 1688. 比赛中的配对次数
class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        if n & 1:
            return n // 2 + self.numberOfMatches((n+1)//2)
        return n // 2 + self.numberOfMatches(n//2)


s = Solution()
n = 7
print(s.numberOfMatches(n))

n = 14
print(s.numberOfMatches(n))

n = 1
print(s.numberOfMatches(n))
