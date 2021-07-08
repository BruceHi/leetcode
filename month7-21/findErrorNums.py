# 645. 错误的集合，返回重复、缺失
# 其余方法不会
from typing import List
from collections import Counter


class Solution:
    # 哈希表
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = [0] * 2
        for i in range(1, len(nums)+1):
            if i not in count:
                res[1] = i
            elif count[i] == 2:
                res[0] = i
        return res

    # # 排序
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    #     nums.sort()
    #     res = [0] * 2
    #
    #     judge = 1  # 求缺失值
    #     for i, num in enumerate(nums[:-1]):
    #         if num == nums[i+1]:
    #             res[0] = num
    #         elif num != judge:
    #             res[1] = judge
    #         judge += 1
    #
    #     # 是否最后一个缺失
    #     if nums[-1] != len(nums):
    #         res[1] = len(nums)
    #     return res


s = Solution()
nums = [1,2,2,4]
print(s.findErrorNums(nums))

nums = [1,1]
print(s.findErrorNums(nums))

nums = [2, 3, 3, 4]
print(s.findErrorNums(nums))

nums = [2, 3, 4, 4]
print(s.findErrorNums(nums))
