from typing import List
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target:
            return 0
        n = len(nums)
        for i in range(1, n):
            if start+i < n and nums[start+i] == target or start-i >= 0 and nums[start-i] == target:
                return i



s = Solution()
nums = [1,2,3,4,5]
target = 5
start = 3
print(s.getMinDistance(nums, target, start))

nums = [1]
target = 1
start = 0
print(s.getMinDistance(nums, target, start))

nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 0
print(s.getMinDistance(nums, target, start))

nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 9
print(s.getMinDistance(nums, target, start))
