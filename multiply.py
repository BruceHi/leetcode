# 两个正整数
class Solution:
    # 不用乘法
    # def multiply(self, A: int, B: int) -> int:
    #     if A > B:
    #         A, B = B, A
    #     res = 0
    #     for _ in range(A):
    #         res += B
    #     return res

    def multiply(self, A: int, B: int) -> int:
        if A == 0 or B == 0:
            return 0
        if A == 1:
            return B
        if B == 1:
            return A
        if A > B:
            A, B = B, A
        return B + self.multiply(A-1, B)


s = Solution()
A = 1
B = 10
print(s.multiply(A, B))

A = 3
B = 4
print(s.multiply(A, B))