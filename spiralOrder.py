from typing import List


class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     res = []
    #     while matrix:
    #         # res += matrix.pop(0)  # 列表后面可以追加元组，相当于 extend
    #         res.extend(matrix.pop(0))
    #         # res = res + matrix.pop(0)  # 列表却不可以连接元组 错误
    #         matrix = list(zip(*matrix))[::-1]
    #     return res

    # 逆时针提取元素，试一试
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix = list(zip(*matrix))  # 转置
        res = list(matrix.pop(0))
        while matrix:
            matrix = list(zip(*matrix))[::-1]
            res += matrix.pop(0)
        return res


s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.spiralOrder(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(matrix))