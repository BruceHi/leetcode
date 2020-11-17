# 旋转矩阵
from typing import List


class Solution:
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     # matrix.reverse()
    #     matrix[:] = map(list, zip(*matrix[::-1]))

    def rotate(self, matrix: List[List[int]]) -> None:
        # matrix[::] = zip(*matrix[::-1])
        a = list(zip(matrix[::-1]))  # 结果：[([7, 8, 9],), ([4, 5, 6],), ([1, 2, 3],)]
        print(a)
        b = list(zip(*matrix[::-1]))  # 结果：[(7, 4, 1), (8, 5, 2), (9, 6, 3)]
        print(b)
        matrix[:] = map(list, zip(*matrix[::-1]))


s = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s.rotate(matrix)
print(matrix)

matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
s.rotate(matrix)
print(matrix)

# a = {1, 2, 4}
# # a += {5, 6, 7}
# a += 8, 9
# print(a)

a = map(list, ['1', [2], '0'])
print(a)
print(list(a))
