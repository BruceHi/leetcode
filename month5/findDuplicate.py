# 寻找重复数,只有一个重复数，并出现不止一次

from typing import List
from collections import Counter


class Solution:

    # 空间复杂度为 O(n)
    # def findDuplicate(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     key, = [key for key in count if count[key] > 1]
    #     return key
    #     # for key, val in count.items():
    #     #     if val > 1:
    #     #         return key

    # def findDuplicate(self, nums: List[int]) -> int:
    #     hash_map = {}
    #     for num in nums:
    #         hash_map[num] = hash_map.get(num, 0) + 1
    #         if hash_map[num] > 1:
    #             return num
    #

    # 时间复杂度为 O(n^2)
    # def findDuplicate(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     for i in range(1, n):
    #         res = nums.count(i)
    #         if res > 1:
    #             return i

    # def findDuplicate(self, nums: List[int]) -> int:
    #     slow, fast = nums[0], nums[nums[0]]
    #     while slow != fast:
    #         slow = nums[slow]
    #         fast = nums[nums[fast]]
    #
    #     find = 0
    #     while find != slow:
    #         find, slow = nums[find], nums[slow]
    #     return find

    # def findDuplicate(self, nums: List[int]) -> int:
    #     slow, fast = nums[0], nums[nums[0]]
    #     while slow != fast:
    #         slow = nums[slow]
    #         fast = nums[nums[fast]]
    #
    #     find = 0
    #     while find != slow:
    #         find = nums[find]
    #         slow = nums[slow]
    #     return find

    # def findDuplicate(self, nums: List[int]) -> int:
    #     slow, fast = nums[0], nums[nums[0]]
    #     while slow != fast:
    #         slow = nums[slow]
    #         fast = nums[nums[fast]]
    #
    #     find = 0  # 从 0 开始
    #     while find != slow:
    #         find, slow = nums[find], nums[slow]
    #     return find

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]  # 初始值是 slow 已经走了一步，fast 已经走了两步。
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        find = 0  # 注意开始的地方
        while find != slow:
            find, slow = nums[find], nums[slow]
        return find




s = Solution()
nums = [1,3,4,2,2]
print(s.findDuplicate(nums))

nums = [3,1,3,4,2]
print(s.findDuplicate(nums))

nums = [1, 2, 1]
print(s.findDuplicate(nums))
