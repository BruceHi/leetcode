# 46. 全排列，没有重复的数字
from typing import List
from itertools import permutations


class Solution:
    # 回溯
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     n = len(nums)
    #
    #     def dfs(nums, cur):
    #         if len(cur) == n:
    #             res.append(cur)
    #             return
    #         for num in nums:
    #             if num not in cur:  # 判断是否存在
    #                 dfs(nums, cur+[num])
    #
    #     dfs(nums, [])
    #     return res

    # 回溯，每次选择好之后就将当前的值删掉。更推荐这个。
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, cur):
            if not nums:
                res.append(cur)
                return

            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], cur+[nums[i]])

        dfs(nums, [])
        return res

    # 使用内置函数，生成全排列
    def permute(self, nums: List[int]) -> List[List[int]]:
        # permutations(nums) 为迭代器对象
        # return list(permutations(nums))
        return list(map(list, permutations(nums)))


s = Solution()
print(s.permute([1,2,3]))

a = [1]
b = a + [2]
print(id(a))
print(id(b))

a += [2]
print(id(a))
