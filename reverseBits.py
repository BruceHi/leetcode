# 190.颠倒二进制位
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n >> i & 1
            res = res * 2 + bit
        return res


s = Solution()
n = 0b0000010100101000001111010011100
print(type(n))
print(s.reverseBits(n))


n = 0b11111111111111111111111111111101
print(type(n))
print(s.reverseBits(n))
