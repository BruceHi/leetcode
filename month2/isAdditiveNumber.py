# 306. 累加数
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False

        def dfs(i, j, cur):
            pass





s = Solution()
num = "112358"
print(s.isAdditiveNumber(num))

num = "199100199"
print(s.isAdditiveNumber(num))
