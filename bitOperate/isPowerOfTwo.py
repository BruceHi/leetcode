# 2 的幂
class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if not n:
    #         return False
    #     if n == 1:
    #         return True
    #     if n % 2:
    #         return False
    #     return self.isPowerOfTwo(n >> 1)

    # 使用位运算
    # def isPowerOfTwo(self, n: int) -> bool:
    #     return n > 0 and not n & n-1

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n & (n-1)


s = Solution()

print(s.isPowerOfTwo(0))

print(s.isPowerOfTwo(1))

print(s.isPowerOfTwo(16))

print(s.isPowerOfTwo(218))
