# 476. 数字的补数
class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)
        num = ''.join(map(lambda x: str(int(x) ^ 1), b[2:]))
        return int(num, base=2)


s = Solution()
num = 5
print(s.findComplement(num))

num = 1
print(s.findComplement(num))
