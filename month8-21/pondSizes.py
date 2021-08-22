# 面试题 16.19. 水域大小
from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])

        def dfs(i, j):
            land[i][j] = 1
            res = 1
            for dx in [0, -1, 1]:
                for dy in [0, -1, 1]:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and land[x][y] == 0:
                        res += dfs(x, y)
            return res

        ans = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    ans.append(dfs(i, j))
        return sorted(ans)


s = Solution()
land = [
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
print(s.pondSizes(land))
