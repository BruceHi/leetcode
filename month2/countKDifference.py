# 2006. 差的绝对值为 k 的数对数目
from typing import List
from collections import defaultdict


class Solution:
    # def countKDifference(self, nums: List[int], k: int) -> int:
    #     res = 0
    #     n = len(nums)
    #     for i in range(0, n-1):
    #         for j in range(i+1, n):
    #             if abs(nums[i]-nums[j]) == k:
    #                 res += 1
    #     return res

    # 哈希表
    def countKDifference(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        res = 0
        for num in nums:
            res += dic[num-k] + dic[num+k]
            dic[num] += 1
        return res


s = Solution()
nums = [1,2,2,1]
k = 1
print(s.countKDifference(nums, k))

nums = [1,3]
k = 3
print(s.countKDifference(nums, k))

nums = [3,2,1,5,4]
k = 2
print(s.countKDifference(nums, k))
