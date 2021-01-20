# 组合总和3
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        def dfs(cur, cur_sum):
            if len(cur) == k and cur_sum == n:
                res.append(cur)
                return
            if len(cur) > k or cur_sum > n:
                return
            for i in range(1, 10):
                if not cur or i > cur[-1]:  # cur 不存在，若存在，i 必须大于最后一个
                    dfs(cur + [i], cur_sum + i)

        dfs([], 0)
        return res




s = Solution()
k = 3
n = 7
print(s.combinationSum3(k, n))

k = 3
n = 9
print(s.combinationSum3(k, n))
