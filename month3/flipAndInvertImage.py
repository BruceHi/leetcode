# 832. 翻转图像
from typing import List


class Solution:
    # def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    #     flip = [x[::-1] for x in image]
    #     res = []
    #     for row in flip:
    #         cur = []
    #         for a in row:
    #             cur.append(1 ^ a)
    #         res.append(cur)
    #     return res

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 ^ x for x in row[::-1]] for row in image]


s = Solution()
image = [[1,1,0],[1,0,1],[0,0,0]]
print(s.flipAndInvertImage(image))

image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(s.flipAndInvertImage(image))
