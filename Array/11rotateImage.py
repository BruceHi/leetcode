# 将图像顺时针旋转 90 度。

# 观察规律
# def rotate(matrix):
#     n = len(matrix)
#     matrix.reverse()
#
#     for j in range(n):  # 提取元素
#         temp = [matrix[i][j] for i in range(n)]
#         matrix.append(temp)
#
#     for i in range(n-1, -1, -1):  # 删除元素
#         matrix.pop(i)


# def rotate(matrix):
#     matrix[:] = map(list, zip(*(matrix[::-1])))


# 先转置再说
def rotate(matrix):
    matrix[:] = list(map(list, zip(*matrix)))

    for lst in matrix:
        lst.reverse()


# def rotate(matrix):
#     n = len(matrix)
#
#     for i in range(n):  # 转置
#         for j in range(i+1, n):
#             matrix[i][j], matrix[j][i] \
#                     = matrix[j][i], matrix[i][j]
#
#     for i in range(n):  # 交换顺序
#         matrix[i].reverse()


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(matrix1)
print(matrix1)
#  [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# 反向列表
# [
#  [7, 8, 9],
#  [4, 5, 6],
#  [1, 2, 3]
# ]

# 竖列提取元素
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]


matrix1 = [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
]

# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
rotate(matrix1)
print(matrix1)
