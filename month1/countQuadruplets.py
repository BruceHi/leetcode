# 1995. 统计特殊四元组
from typing import List
from collections import Counter


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        def add_one(old: Counter, new: Counter, num):
            for k, v in old.items():
                new[k+num] += v

        dic1, dic2, dic3 = Counter(), Counter(), Counter()
        res = 0
        for i, num in enumerate(nums):
            if i == 0:
                dic1[num] += 1
            elif i == 1:
                add_one(dic1, dic2, num)
                dic1[num] += 1
            elif i == 2:
                add_one(dic2, dic3, num)
                add_one(dic1, dic2, num)
                dic1[num] += 1
            else:
                if num in dic3:
                    res += dic3[num]
                add_one(dic2, dic3, num)
                add_one(dic1, dic2, num)
                dic1[num] += 1
        return res



s = Solution()
nums = [1,2,3,6]
print(s.countQuadruplets(nums))

nums = [3,3,6,4,5]
print(s.countQuadruplets(nums))

nums = [1,1,1,3,5]
print(s.countQuadruplets(nums))
