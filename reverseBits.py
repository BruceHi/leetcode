# 190.颠倒二进制位
class Solution:
    def reverseBits(self, n: int) -> int:
        print(str(int(n)))
        print(int(''.join(reversed(str(int(n))))))
        return bin(int(''.join(reversed(str(int(n))))))


s = Solution()
n = 0b0000010100101000001111010011100
print(type(n))
print(s.reverseBits(n))


n = 0b11111111111111111111111111111101
print(type(n))
print(s.reverseBits(n))