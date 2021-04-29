class Solution:
    # def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
    #     matrix = [[0] * num for _ in range(num)]
    #     print(matrix[0])
    #
    #     matrix[0] = list(range(1, 10)) * (num // 9)
    #     matrix[0].extend(range(1, num%9+1))
    #
    #     print(matrix)

    # 超时
    # def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
    #     matrix = [[0] * num for _ in range(num)]
    #     l, r, t, b = 0, num-1, 0, num-1
    #     k = 0
    #     while True:
    #         for i in range(l, r+1):
    #             matrix[t][i] = k+1
    #             k = (k+1) % 9
    #         if matrix[xPos][yPos]:
    #             return matrix[xPos][yPos]
    #         t += 1
    #         if t > b:
    #             break
    #
    #         for i in range(t, b+1):
    #             matrix[i][r] = k+1
    #             k = (k+1) % 9
    #         if matrix[xPos][yPos]:
    #             return matrix[xPos][yPos]
    #         r -= 1
    #         if l > r:
    #             break
    #
    #         for i in range(r, l-1, -1):
    #             matrix[b][i] = k+1
    #             k = (k+1) % 9
    #         if matrix[xPos][yPos]:
    #             return matrix[xPos][yPos]
    #         b -= 1
    #         if t > b:
    #             break
    #
    #         for i in range(b, t-1, -1):
    #             matrix[i][l] = k+1
    #             k = (k+1) % 9
    #         if matrix[xPos][yPos]:
    #             return matrix[xPos][yPos]
    #         l += 1
    #         if l > r:
    #             break

    # 又超时了
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        if xPos == 0:
            return yPos % 9 + 1
        matrix = [[0] * num for _ in range(num)]
        l, r, t, b = 0, num-1, 0, num-1
        k = 0
        while True:
            for i in range(l, r+1):
                matrix[t][i] = k+1
                k = (k+1) % 9
            t += 1
            if t > b:
                break

            for i in range(t, b+1):
                matrix[i][r] = k+1
                k = (k+1) % 9
            r -= 1
            if l > r:
                break

            for i in range(r, l-1, -1):
                matrix[b][i] = k+1
                k = (k+1) % 9
            b -= 1
            if t > b:
                break

            for i in range(b, t-1, -1):
                matrix[i][l] = k+1
                k = (k+1) % 9
            l += 1
            if l > r:
                break

        return matrix[xPos][yPos]


s = Solution()
num = 3
Xpos = 0
Ypos = 2
print(s.orchestraLayout(num, Xpos, Ypos))

num = 4
Xpos = 1
Ypos = 2
print(s.orchestraLayout(num, Xpos, Ypos))

num = 1
Xpos = 0
Ypos = 0
print(s.orchestraLayout(num, Xpos, Ypos))
