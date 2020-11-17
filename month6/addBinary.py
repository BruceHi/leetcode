# 二进制求和
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # {：b} 可以将 int 转换为 不含前导 ‘0b’ 的二进制字符串
        return '{:b}'.format(int(a, 2) + int(b, 2))

    # def addBinary(self, a: str, b: str) -> str:
    #     # bin(x): x 为 int类型，结果返回带有 ‘0b’ 的字符串类型
    #     return bin(int(a, 2) + int(b, 2))[2:]


s = Solution()
a = "11"
b = "1"
print(s.addBinary(a, b))

a = "1010"
b = "1011"
print(s.addBinary(a, b))
