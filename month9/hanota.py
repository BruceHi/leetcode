# 面试题 08.06. 汉诺塔问题
from typing import List


class Solution:
    # def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
    #     if len(A) == 1:
    #         C.append(A.pop())
    #         return
    #     B.append(A.pop())
    #     self.hanota(A, B, C)
    #     C.append(B.pop())

    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        def hanoi(n, A, B, C):
            if n == 1:
                C.append(A.pop())
            else:
                hanoi(n-1, A, C, B)
                C.append(A.pop())
                hanoi(n-1, B, A, C)

        hanoi(len(A), A, B, C)


s = Solution()
A = [2, 1, 0]
B = []
C = []
s.hanota(A, B, C)
print(C)

A = [1, 0]
B = []
C = []
s.hanota(A, B, C)
print(C)
