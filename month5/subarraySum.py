# 和为 k 的子数组
# 要求数组是连续的
from typing import List
from collections import defaultdict


class Solution:

    # # # 暴力法,超出时间限制
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     res = 0
    #     for i in range(len(nums)):
    #         tmp = 0
    #         for num in nums[i:]:
    #             tmp += num
    #             if tmp == k:
    #                 print(i, num)
    #                 res += 1
    #     return res

    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     sum_nums = [sum(nums[i:]) for i in range(len(nums))]
    #     # print(sum_nums)

    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     nums_times = defaultdict(int)
    #     nums_times[0] = 1
    #     pre, res = 0, 0
    #     for num in nums:
    #         pre += num
    #         # if pre_sum - k in nums_times:
    #         #    res += nums_times[pre_sum - k]
    #         res += nums_times[pre - k]
    #         nums_times[pre] += 1
    #     return res

    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     dic = defaultdict(int)
    #     dic[0] = 1
    #     res, pre_sum = 0, 0
    #     for num in nums:
    #         pre_sum += num
    #         res += dic[pre_sum-k]
    #         dic[pre_sum] += 1
    #     return res

    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        res, pre = 0, 0
        for num in nums:
            pre += num
            res += dic[pre-k]
            dic[pre] += 1
        return res


s = Solution()
nums = [2,-2,2]
k = 2
print(s.subarraySum(nums, k))


nums = [1,1,1]
k = 2
print(s.subarraySum(nums, k))


nums = [1, 1, 0, 1, 2]
k = 2
print(s.subarraySum(nums, k))  # 4：[1, 1], [1, 1, 0], [1, 0, 1], [2]

nums = [1, 1, 1, 1, 2]
k = 2
print(s.subarraySum(nums, k))  # 4: [1, 1], [1, 1], [1, 1], [2]
