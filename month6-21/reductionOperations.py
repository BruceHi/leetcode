from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        res = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            res += count
        return res



s = Solution()
nums = [5,1,3]
print(s.reductionOperations(nums))

nums = [1,1,1]
print(s.reductionOperations(nums))

nums = [1,1,2,2,3]
print(s.reductionOperations(nums))

nums = [1,1,2,2,3,5]
print(s.reductionOperations(nums))
