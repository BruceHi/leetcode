# 移除元素
from typing import List


class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     try:
    #         while True:
    #             nums.remove(val)
    #     except ValueError:
    #         return len(nums)

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


s = Solution()
nums = [3,2,2,3]
val = 3
print(s.removeElement(nums, val))
print(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2
print(s.removeElement(nums, val))
print(nums)
