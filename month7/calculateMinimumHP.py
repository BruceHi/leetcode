# 地下城游戏
from typing import List


class Solution:

    # 全错了，操他妈
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        if m == 1 and n == 1:
            return 1
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = dungeon[0][0] if dungeon[0][0] > 0 else -dungeon[0][0]+1

        re = [[0] * n for _ in range(m)]  # 剩余能量
        re[0][0] = dungeon[0][0] if dungeon[0][0] > 0 else 1

        for i in range(1, m):
            tmp = dungeon[i][0] + re[i-1][0]
            if tmp > 0:
                dp[i][0] = dp[i-1][0]
                re[i][0] = tmp
            else:
                dp[i][0] = dp[i - 1][0] - tmp + 1
                re[i][0] = 1

        for j in range(1, n):
            tmp = dungeon[0][j] + re[0][j-1]
            if tmp > 0:
                dp[0][j] = dp[0][j-1]
                re[0][j] = tmp
            else:
                dp[0][j] = dp[0][j-1] - tmp + 1
                re[0][j] = 1
        # return re, dp

        for i in range(1, m):
            for j in range(1, n):
                if dungeon[i][j] < 0:
                    remain1 = re[i][j - 1] + dungeon[i][j]  # 剩余能量
                    if remain1 > 0:
                        tmp1 = dp[i][j-1]
                    else:
                        tmp1 = dp[i][j - 1] - remain1 + 1

                    remain2 = re[i-1][j] + dungeon[i][j]  # 剩余能量
                    if remain2 > 0:
                        tmp2 = dp[i-1][j]
                    else:
                        tmp2 = dp[i-1][j] - remain2 + 1

                    if tmp1 < tmp2:
                        dp[i][j] = tmp1
                        re[i][j] = remain1 if remain1 > 0 else 1
                    else:
                        dp[i][j] = tmp2
                        re[i][j] = remain2 if remain2 > 0 else 1

                else:
                    if dp[i-1][j] < dp[i][j-1]:
                        dp[i][j] = dp[i-1][j]
                        re[i][j] = re[i-1][j] + dungeon[i][j]
                    else:
                        dp[i][j] = dp[i][j-1]
                        re[i][j] = re[i][j-1] + dungeon[i][j]

        return dp[m-1][n-1]


s = Solution()
du = [[-2, -3, 3],
      [-5, -10, 1],
      [10, 30, -5]]
print(s.calculateMinimumHP(du))

du = [[100]]
print(s.calculateMinimumHP(du))
