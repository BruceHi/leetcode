# 1995. 统计特殊四元组
from typing import List
from collections import Counter, defaultdict


class Solution:
    # def countQuadruplets(self, nums: List[int]) -> int:
    #     def add_one(old: Counter, new: Counter, num):
    #         for k, v in old.items():
    #             new[k+num] += v
    #
    #     dic1, dic2, dic3 = Counter(), Counter(), Counter()
    #     res = 0
    #     for i, num in enumerate(nums):
    #         if i == 0:
    #             dic1[num] += 1
    #         elif i == 1:
    #             add_one(dic1, dic2, num)
    #             dic1[num] += 1
    #         elif i == 2:
    #             add_one(dic2, dic3, num)
    #             add_one(dic1, dic2, num)
    #             dic1[num] += 1
    #         else:
    #             if num in dic3:
    #                 res += dic3[num]
    #             add_one(dic2, dic3, num)
    #             add_one(dic1, dic2, num)
    #             dic1[num] += 1
    #     return res

    # 暴力法也能通过
    # def countQuadruplets(self, nums: List[int]) -> int:
    #     res = 0
    #     n = len(nums)
    #     for i in range(n-3):
    #         for j in range(i+1, n-2):
    #             for p in range(j+1, n-1):
    #                 for q in range(p, n):
    #                     if nums[i] + nums[j] + nums[p] == nums[q]:
    #                         res += 1
    #     return res

    # O(n^3)
    # def countQuadruplets(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     res = 0
    #     count = defaultdict(int)
    #     for c in range(n-2, 1, -1):
    #         count[nums[c+1]] += 1  # c+1实际上统计的是 d
    #         for a in range(c-1):
    #             for b in range(a+1, c):
    #                 total = nums[a] + nums[b] + nums[c]
    #                 if total in count:
    #                     res += count[total]
    #     return res

    # O(n^2)
    # nums[a] + nums[b] = nums[d] - nums[c]
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        count = defaultdict(int)
        for b in range(n-3, 0, -1):
            for d in range(b+2, n):
                count[nums[d]-nums[b+1]] += 1  # 统计灯饰右边的，b+1 即是统计 c
            for a in range(b):
                total = nums[a] + nums[b]
                if total in count:
                    res += count[total]
        return res

s = Solution()
nums = [1,2,3,6]
print(s.countQuadruplets(nums))

nums = [3,3,6,4,5]
print(s.countQuadruplets(nums))

nums = [1,1,1,3,5]
print(s.countQuadruplets(nums))
