# 判断有多少个 1
class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     count = 0
    #     while n:
    #         count += 1
    #         n = n & n-1
    #     return count

    # def hammingWeight(self, n: int) -> int:
    #     count = 0
    #     while n:
    #         n &= n-1
    #         count += 1
    #     return count

    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


s = Solution()
a = 0b00000000000000000000000000001011
print(s.hammingWeight(a))

a = 0b00000000000000000000000010000000
print(s.hammingWeight(a))

a = 0b11111111111111111111111111111101
print(s.hammingWeight(a))

a = 0o7
print(bin(a))
print(type(a))

a = 0o7
print(int(a))
print(type(a))

a = 0b10101
print(int(a))
print(type(a))
