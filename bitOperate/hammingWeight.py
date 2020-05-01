# 判断有多少个 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = n & n-1
        return count


s = Solution()
a = 0b00000000000000000000000000001011
print(s.hammingWeight(a))

a = 0b00000000000000000000000010000000
print(s.hammingWeight(a))

a = 0b11111111111111111111111111111101
print(s.hammingWeight(a))
