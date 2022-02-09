# 334. 递增的三元子序列
# 贪心法
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first, second = nums[0], float('inf')
        for num in nums[1:]:  # 寻找第三个
            if num > second:
                return True
            if num > first:
                second = num
            else:
                first = num
        return False




s = Solution()
nums = [1,2,3,4,5]
print(s.increasingTriplet(nums))

nums = [5,4,3,2,1]
print(s.increasingTriplet(nums))

nums = [2,1,5,0,4,6]
print(s.increasingTriplet(nums))

nums = [20,100,10,12,5,13]
print(s.increasingTriplet(nums))

nums = [1,5,0,4,1,3]
print(s.increasingTriplet(nums))

nums = [2,4,-2,-3]
print(s.increasingTriplet(nums))

