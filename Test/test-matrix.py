def func(matrix):
    if matrix[1][2] > matrix[2][2]:
        return matrix
    matrix[1][1], matrix[2][1] = matrix[2][1], matrix[1][1]
    matrix[1][2], matrix[2][2] = matrix[2][2], matrix[1][2]
    return matrix




a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
print(func(a))

# def func2(matrix, begin_r, end_r, begin_c, end_c, way):



