# 1365. 有多少小于当前数字的数字
from typing import List
from collections import Counter
from collections import defaultdict


class Solution:

    # 本质还是暴力求解
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     dic = Counter(nums)
    #     res = []
    #     for num in nums:
    #         res.append(sum(val for key, val in dic.items() if key < num))
    #     return res

    # # 时间复杂度依旧为 O(n^2)，index 函数所用时间为 O(n)
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     arrs = sorted(nums)
    #     return [arrs.index(num) for num in nums]

    # 时间复杂度为 O(nlogn)
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     arrs = sorted(nums)
    #     dic = {}
    #     for i, num in enumerate(arrs):
    #         if num not in dic:  # 排除重复的干扰-
    #             dic[num] = i
    #     return [dic[num] for num in nums]

    # 计数排序，时间复杂度 O(N + M)，空间复杂度 O(M)
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     count = [0] * 101
    #     for num in nums:
    #         count[num] += 1
    #
    #     for i in range(1, 101):
    #         count[i] += count[i-1]
    #
    #     # # 当 num 为 0 时，出现错误
    #     # return [count[num-1] for num in nums]
    #     res = [0] * len(nums)
    #     for i, num in enumerate(nums):
    #         if num:
    #             res[i] = count[num-1]
    #     return res

    # 时间复杂度为 O(nlogn)
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     count = Counter(nums)
    #     arrs = list(count)
    #     arrs.sort()
    #
    #     dic = {}
    #     total = 0
    #     for num in arrs:
    #         dic[num] = total
    #         total += count[num]
    #
    #     res = []
    #     for num in nums:
    #         res.append(dic[num])
    #     return res


    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        dic = {}
        for i, num in enumerate(arr):
            if num not in dic:
                dic[num] = i
        return [dic[num] for num in nums]


s = Solution()
nums = [8,1,2,2,3]
print(s.smallerNumbersThanCurrent(nums))

nums = [6,5,4,8]
print(s.smallerNumbersThanCurrent(nums))

nums = [7,7,7,7]
print(s.smallerNumbersThanCurrent(nums))

nums = [5,0,10,0,10,6]
print(s.smallerNumbersThanCurrent(nums))
