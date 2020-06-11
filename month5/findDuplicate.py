# 寻找重复数,只有一个重复数，并出现不止一次

from typing import List
from collections import Counter


class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     for key, val in count.items():
    #         if val > 1:
    #             return key

    # def findDuplicate(self, nums: List[int]) -> int:
    #     hash_map = {}
    #     for num in nums:
    #         hash_map[num] = hash_map.get(num, 0) + 1
    #         if hash_map[num] > 1:
    #             return num

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        find = 0
        while find != slow:
            find, slow = nums[find], nums[slow]
        return find


s = Solution()
nums = [1,3,4,2,2]
print(s.findDuplicate(nums))

nums = [3,1,3,4,2]
print(s.findDuplicate(nums))