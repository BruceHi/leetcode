# 二进制求和
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{:b}'.format(int(a, 2) + int(b, 2))


s = Solution()
a = "11"
b = "1"
print(s.addBinary(a, b))

a = "1010"
b = "1011"
print(s.addBinary(a, b))
