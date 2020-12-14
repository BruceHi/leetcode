# 190.颠倒二进制位
class Solution:
    # def reverseBits(self, n: int) -> int:
    #     res = 0
    #     for i in range(32):
    #         bit = n >> i & 1
    #         res = res * 2 + bit
    #     return res

    def reverseBits(self, n: int) -> int:
        # 格式化字符串：0表示前面补 0，32表示长度，b 表示二进制。
        return int(f'{n:032b}'[::-1], 2)


s = Solution()
n = 0b0000010100101000001111010011100
print(type(n))
print(s.reverseBits(n))


n = 0b11111111111111111111111111111101
print(type(n))
print(s.reverseBits(n))
