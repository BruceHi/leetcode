# 整数拆分
class Solution:
    # def integerBreak(self, n: int) -> int:
    #     if n <= 3:
    #         return n-1
    #     a, b = divmod(n, 3)
    #     if not b:
    #         return 3 ** a
    #     if b == 1:
    #         return 3 ** (a-1) * 4
    #     if b == 2:
    #         return 3 ** a * b

    # def integerBreak(self, n: int) -> int:
    #     if n <= 3:
    #         return n-1
    #     if n % 3 == 1:
    #         return 3 ** (n//3-1) * 4
    #     if n % 3 == 2:
    #         return 3 ** (n//3) * 2
    #     return 3 ** (n//3)

    # Python 中常见有三种幂计算函数： * 和 pow() 的时间复杂度均为 O(\log a)O(loga) ；
    # 而 math.pow() 始终调用 C 库的 pow() 函数，其执行浮点取幂，时间复杂度为 O(1)O(1) 。
    # 链接：https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        a, b = divmod(n, 3)
        if b == 1:
            return 3 ** (a-1) * 4
        if b == 2:
            return 3 ** a * 2
        return 3 ** a


s = Solution()
print(s.integerBreak(2))

print(s.integerBreak(10))
