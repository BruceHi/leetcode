# 461.汉明距离
class Solution:
    # def hammingDistance(self, x: int, y: int) -> int:
    #     dist = x ^ y
    #     res = 0
    #     while dist:
    #         res += 1
    #         dist &= dist - 1
    #     return res

    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


s = Solution()
x = 1
y = 4
print(s.hammingDistance(x, y))