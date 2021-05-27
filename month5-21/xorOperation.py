# 1486. 数组的异或操作
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res


s = Solution()
n = 5
start = 0
print(s.xorOperation(n, start))

n = 4
start = 3
print(s.xorOperation(n, start))

n = 1
start = 7
print(s.xorOperation(n, start))

n = 10
start = 5
print(s.xorOperation(n, start))
