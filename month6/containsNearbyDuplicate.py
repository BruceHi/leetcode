# 存在重复元素 II
from typing import List


class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     dic = {}
    #     for i, num in enumerate(nums):
    #         if num in dic and i - dic[num] <= k:
    #             return True
    #         dic[num] = i
    #     return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        dic = {}
        for i, num in enumerate(nums):
            if num in dic and i - dic[num] <= k:
                return True
            dic[num] = i
        return False




s = Solution()
nums = [1,2,3,1]
k = 3
print(s.containsNearbyDuplicate(nums, k))

nums = [1,0,1,1]
k = 1
print(s.containsNearbyDuplicate(nums, k))

nums = [1,2,3,1,2,3]
k = 2
print(s.containsNearbyDuplicate(nums, k))

nums = []
k = 0
print(s.containsNearbyDuplicate(nums, k))