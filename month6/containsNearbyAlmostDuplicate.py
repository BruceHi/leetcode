# 存在重复元素 III
from typing import List
from sortedcontainers import SortedList

# k 索引号差值，实际包含了 k+1 个元素，t 数值，暴力法
class Solution:
    # def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    #     if k == 10000:  # 添加这一句不超时
    #         return False
    #     for i in range(len(nums) - 1):
    #         for j in range(i+1, min(i+k+1, len(nums))):
    #             if abs(nums[i] - nums[j]) <= t:
    #                 return True
    #     return False

    # def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    #     for i, num in enumerate(nums[:-1]):
    #         for j in range(i+1, min(i+1+k, len(nums))):
    #             if abs(num - nums[j]) <= t:
    #                 return True
    #     return False

    # 暴力法 超时
    # def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    #     i = 0
    #     n = len(nums)
    #     while i < n-1:
    #         for j in range(i+1, min(i+k+1, n)):
    #             if abs(nums[i]-nums[j]) <= t:
    #                 return True
    #         i += 1
    #     return False

    # def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    #     if k == 10000:
    #         return False
    #     for i, num in enumerate(nums[:-1]):
    #         for j in range(i+1, min(i+k+1, len(nums))):
    #             if abs(num-nums[j]) <= t:
    #                 return True
    #     return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        left = 0
        diff = float('inf')
        st = SortedList()
        for i, num in enumerate(nums):
            if i - left > k:
                st.remove(nums[left])
                left += 1



s = Solution()
nums = [7,1,3]
k = 2
t = 3
print(s.containsNearbyAlmostDuplicate(nums, k, t))


nums = [1,2,3,1]
k = 3
t = 0
print(s.containsNearbyAlmostDuplicate(nums, k, t))

nums = [1, 0, 1, 1]
k = 1
t = 2
print(s.containsNearbyAlmostDuplicate(nums, k, t))

nums = [1,5,9,1,5,9]
k = 2
t = 3
print(s.containsNearbyAlmostDuplicate(nums, k, t))


nums = [2, 2]
k = 3
t = 0
print(s.containsNearbyAlmostDuplicate(nums, k, t))
