# 78. 子集
from typing import List
from itertools import combinations


class Solution:
    # 库函数
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     for i in range(len(nums)+1):
    #         # tmp = list(map(list, combinations(nums, i)))  # 不用 list 完全可以，extend 只需要迭代器
    #         tmp = map(list, combinations(nums, i))
    #         res.extend(tmp)
    #     return res

    # 迭代
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]
    #     for num in nums:
    #         # res.extend([num] + tmp for tmp in res)  # 死循环，res 会不断增长的。
    #         res += [[num] + tmp for tmp in res]
    #     return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            res.extend(map(list, combinations(nums, i)))
        return res



s = Solution()
nums = [1,2,3]
print(s.subsets(nums))

# a = combinations([1, 2], 0)
# print(list(a))
#
# a = combinations([1, 2], 2)
# print(list(a))
