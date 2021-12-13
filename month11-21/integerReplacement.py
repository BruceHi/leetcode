# 397. 整数替换
from functools import lru_cache


class Solution:
    # 使用 lru 快得多
    @lru_cache(None)
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2:
            return min(self.integerReplacement(n+1), self.integerReplacement(n-1)) + 1
        return 1 + self.integerReplacement(n//2)


s = Solution()
n = 8
print(s.integerReplacement(n))

n = 7
print(s.integerReplacement(n))

n = 4
print(s.integerReplacement(n))
