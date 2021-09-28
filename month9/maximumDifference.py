from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if nums == sorted(nums, reverse=True):
            return -1

        res = 0
        min_v = nums[0]
        for i in range(1, len(nums)):
            res = max(res, nums[i]-min_v)
            min_v = min(min_v, nums[i])
        return res


s = Solution()
nums = [7,1,5,4]
print(s.maximumDifference(nums))

nums = [9,4,3,2]
print(s.maximumDifference(nums))

nums = [1,5,2,10]
print(s.maximumDifference(nums))

nums = [2, 2]
print(s.maximumDifference(nums))