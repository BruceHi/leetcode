# 80.删除排序数组中的重复项 2
from typing import List


class Solution:
    # 最多重复两次
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     i = 0
    #     for num in nums:
    #         if i < 2 or num != nums[i-2]:
    #             nums[i] = num
    #             i += 1
    #     return i

    # 最多重复 k 次
    # def removeDuplicates(self, nums: List[int], k) -> int:
    #     i = 0
    #     for num in nums:
    #         if i < k or num != nums[i-k]:
    #             nums[i] = num
    #             i += 1
    #     return i


    # def removeDuplicates(self, nums: List[int]) -> int:
    #     i = 0
    #     for num in nums:
    #         if i < 2 or num != nums[i-2]:
    #             nums[i] = num
    #             i += 1
    #     return i

    # def removeDuplicates(self, nums: List[int]) -> int:
    #     i = 0
    #     for num in nums:
    #         if i < 2 or num != nums[i-2]:
    #             nums[i] = num
    #             i += 1
    #     return i

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or num != nums[i-2]:
                nums[i] = num
                i += 1
        return i


s = Solution()
nums = [1,1,1,2,2,3]
print(s.removeDuplicates(nums))
print(nums)

nums = [0,0,1,1,1,1,2,3,3]
print(s.removeDuplicates(nums))
print(nums)
