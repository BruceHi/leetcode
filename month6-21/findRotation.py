from typing import List


class Solution:
    # def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
    #     def rotation(mat):
    #         return list(map(lambda x : list(x[::-1]), zip(*mat)))
    #     if mat == target:
    #         return True
    #     mat1 = rotation(mat)
    #     if mat1 == target:
    #         return True
    #     mat2 = rotation(mat1)
    #     if mat2 == target:
    #         return True
    #     mat3 = rotation(mat2)
    #     if mat3 == target:
    #         return True
    #     return False

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotation(mat):
            return list(map(list, zip(*mat[::-1])))
        if mat == target:
            return True
        mat1 = rotation(mat)
        if mat1 == target:
            return True
        mat2 = rotation(mat1)
        if mat2 == target:
            return True
        mat3 = rotation(mat2)
        if mat3 == target:
            return True
        return False

s = Solution()
mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
print(s.findRotation(mat, target))

mat = [[0,1],[1,1]]
target = [[1,0],[0,1]]
print(s.findRotation(mat, target))

mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
print(s.findRotation(mat, target))
