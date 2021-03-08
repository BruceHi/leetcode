# 674. 最长连续递增序列
# 善用 start 开始
from typing import List


class Solution:
    # def findLengthOfLCIS(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     res = 1
    #     count = 1
    #     for i, num in enumerate(nums[:-1]):
    #         if nums[i+1] > num:
    #             count += 1
    #         else:
    #             res = max(res, count)
    #             count = 1
    #     res = max(res, count)
    #     return res

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start, res = 0, 0
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] >= num:
                start = i
            res = max(res, i-start+1)
        return res


s = Solution()
nums = [1,3,5,4,7]
print(s.findLengthOfLCIS(nums))

nums = [2,2,2,2,2]
print(s.findLengthOfLCIS(nums))

nums = [1, 3, 5, 7]
print(s.findLengthOfLCIS(nums))

nums = []
print(s.findLengthOfLCIS(nums))

nums = [1,3,5,4,2,3,4,5]
print(s.findLengthOfLCIS(nums))

