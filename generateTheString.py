# 1374. 生成每种字符都是奇数个的字符串

class Solution:
    def generateTheString(self, n: int) -> str:
        if n & 1:
            return 'a' * n
        return 'a' + 'b' * (n-1)


s = Solution()
print(s.generateTheString(4))

print(s.generateTheString(2))

print(s.generateTheString(7))
