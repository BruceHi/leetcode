from typing import List


class Solution:
    # def gridGame(self, grid: List[List[int]]) -> int:
    #     n = len(grid[0])
    #     dp = [[0] * (n+1) for _ in range(3)]
    #     nums = []
    #     for i in range(1, 3):
    #         for j in range(1, n+1):
    #             dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
    #     print(nums)
    #     print(dp)
    #     return dp[2][n]

    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp = [[0] * (n+1) for _ in range(3)]
        for i in range(1, 3):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

        # op = [[0] * n for _ in range(2)]
        # op[0] = dp[1][1:]
        # op[1] = dp[2][1:]
        #
        # res = []
        # i, j = 1, n-1
        # while i > 0 and j > 0:
        #     res.append([i, j])
        #     if op[i-1][j]


        nums = []
        i, j = 1, n-1
        while i >= 0 and j >= 0:
            nums.append([i, j])
            if dp[i][j+1] + grid[i][j] == dp[i+1][j+1]:
                i -= 1
            else:
                j -= 1

        print(dp[2][n], nums)
        for i, j in nums:
            grid[i][j] = 0


        dp = [[0] * (n+1) for _ in range(3)]
        for i in range(1, 3):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

        return dp[2][n]


s = Solution()
grid = [[2,5,4],[1,5,1]]
print(s.gridGame(grid))

grid = [[3,3,1],[8,5,2]]
print(s.gridGame(grid))

grid = [[1,3,1,15],[1,3,3,1]]
print(s.gridGame(grid))

grid = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]
print(s.gridGame(grid))
