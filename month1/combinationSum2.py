# 40. 组合总和2
# 原数组有重复的数
# candidates 中的每个数字在每个组合中只能使用一次。
# 组合不能重复
from typing import List


class Solution:
    # 超时
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     if sum(candidates) < target or min(candidates) > target:
    #         return []
    #     candidates.sort()
    #     n = len(candidates)
    #
    #     res = []
    #
    #     def dfs(i, cur, remain):
    #         if remain == 0:
    #             if cur not in res:
    #                 res.append(cur)
    #             return
    #         if remain < 0:
    #             return
    #         for j in range(i, n):
    #             dfs(j+1, cur+[candidates[j]], remain-candidates[j])
    #     dfs(0, [], target)
    #     return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # if sum(candidates) < target or min(candidates) > target:
        #     return []
        candidates.sort()
        res = []

        def dfs(nums, i, cur, remain):  # i：开始选取的位置
            if remain == 0:
                res.append(cur)
                return
            if remain < 0:
                return
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:  # 在递归中判断是否相同，高
                    continue
                dfs(nums, j+1, cur+[candidates[j]], remain-candidates[j])

        dfs(candidates, 0, [], target)
        return res


s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(s.combinationSum2(candidates, target))

candidates = [2,5,2,1,2]
target = 5
print(s.combinationSum2(candidates, target))

candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 27
print(s.combinationSum2(candidates, target))