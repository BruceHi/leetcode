# 和为 k 的子数组
# 要求数组是连续的
from typing import List
from collections import defaultdict


class Solution:

    # # 暴力法,超出时间限制
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     res = 0
    #     for i in range(len(nums)):
    #         tmp = 0
    #         for j in nums[i:]:
    #             tmp += j
    #             if tmp == k:
    #                 res += 1
    #     return res

    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     sum_nums = [sum(nums[i:]) for i in range(len(nums))]
    #     # print(sum_nums)

    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_times = defaultdict(int)
        nums_times[0] = 1
        pre_sum, res = 0, 0
        for num in nums:
            pre_sum += num
            # if pre_sum - k in nums_times:
            #    res += nums_times[pre_sum - k]
            res += nums_times[pre_sum - k]
            nums_times[pre_sum] += 1
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
print(s.subarraySum(nums, k))