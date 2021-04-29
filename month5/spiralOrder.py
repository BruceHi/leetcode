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
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     matrix = list(zip(*matrix))  # 转置
    #     res = list(matrix.pop(0))
    #     while matrix:
    #         matrix = list(zip(*matrix))[::-1]
    #         res += matrix.pop(0)
    #     return res

    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     res = matrix.pop(0)
    #     while matrix:
    #         matrix[:] = list(map(list, zip(*matrix)))[::-1]
    #         res += matrix.pop(0)
    #     return res

    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     res = []
    #     while matrix:
    #         res += matrix.pop(0)
    #         matrix = list(zip(*matrix))[::-1]
    #     return res

    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     res = []
    #     while matrix:
    #         res.extend(matrix.pop(0))
    #         matrix = list(zip(*matrix))[::-1]
    #     return res

    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     if not matrix:
    #         return []
    #     res = []
    #     l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    #     while True:
    #         for i in range(l, r+1):
    #             res.append(matrix[t][i])
    #         t += 1
    #         if t > b:
    #             break
    #
    #         for i in range(t, b+1):
    #             res.append(matrix[i][r])
    #         r -= 1
    #         if l > r:
    #             break
    #
    #         for i in range(r, l-1, -1):
    #             res.append(matrix[b][i])
    #         b -= 1
    #         if t > b:
    #             break
    #
    #         for i in range(b, t-1, -1):
    #             res.append(matrix[i][l])
    #         l += 1
    #         if l > r:
    #             break
    #     return res

    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     res = []
    #     while matrix:
    #         res.extend(matrix.pop(0))
    #         matrix[:] = list(zip(*matrix))[::-1]
    #     return res


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, r, t, b = 0, n-1, 0, m-1
        res = []
        while True:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break

            for j in range(t, b+1):
                res.append(matrix[j][r])
            r -= 1
            if l > r:
                break

            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break

            for j in range(b, t-1, -1):
                res.append(matrix[j][l])
            l += 1
            if l > r:
                break
        return res



s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.spiralOrder(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(matrix))
