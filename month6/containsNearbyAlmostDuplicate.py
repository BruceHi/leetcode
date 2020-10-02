# 存在重复元素 III
from typing import List

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

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i, num in enumerate(nums[:-1]):
            for j in range(i+1, min(i+1+k, len(nums))):
                if abs(num - nums[j]) <= t:
                    return True
        return False


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
