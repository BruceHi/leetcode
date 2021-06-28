# 81. 搜索旋转排序数组 2
# 有重复数出现
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            # 处理左右边界重复数字，只保留一个
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            mid = left + right >> 1
            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False



s = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
print(s.search(nums, target))

nums = [2,5,6,0,0,1,2]
target = 3
print(s.search(nums, target))
