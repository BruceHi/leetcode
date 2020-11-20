# 39. 组合总数
# 如果题目要求，结果集不计算顺序，此时需要按顺序搜索，才能做到不重不漏。
# 「力扣」第 47 题（ 全排列 II ）、「力扣」第 15 题（ 三数之和 ）也使用了类似的思想，使得结果集没有重复。

from typing import List


class Solution:
    # 使用排序的方式判重
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     res = []
    #     min_val = min(candidates)
    #
    #     def dfs(nums, cur, remain):
    #         if remain == 0:
    #             if sorted(cur) not in res:
    #                 res.append(sorted(cur))
    #             return
    #         if remain < min_val:  # 剩余的元素比最小值都要小，退出回溯
    #             return
    #         for num in nums:
    #             dfs(nums, cur + [num], remain-num)
    #     dfs(candidates, [], target)
    #
    #     return res

    # 顺序搜索判重，利用题目强调的 无重复元素
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def dfs(nums, idx, cur, remain):  # idx 开始搜索的位置
            if remain == 0:
                res.append(cur)
                return
            if remain < 0:  # 和上面我的思想差不多，只是这次和 0 比较。比我上面的多回溯了一遍。这种方法更简洁。
                return
            for i in range(idx, n):
                dfs(nums, i, cur + [nums[i]], remain-nums[i])

        dfs(candidates, 0, [], target)
        return res


s = Solution()
candidates = [2,3,6,7]
target = 7
print(s.combinationSum(candidates, target))

candidates = [2,3,5]
target = 8
print(s.combinationSum(candidates, target))

# 元素位置不一样的列表不相同。
print([1, 2, 3] == [2, 3, 1])
# TypeError: unhashable type: 'list'，集合里面不能放列表，所以不能用 set 判重。
