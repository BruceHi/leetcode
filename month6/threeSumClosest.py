#  最接近的三数之和
from typing import List
import bisect


class Solution:
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     if n == 3:
    #         return sum(nums)
    #     nums.sort()
    #     res, diff = 0, float('inf')
    #     for i, num in enumerate(nums[:-2]):
    #         left, right = i + 1, n - 1
    #         while left < right:
    #             cur = num + nums[left] + nums[right]
    #             if cur < target:
    #                 left += 1
    #             elif cur > target:
    #                 right -= 1
    #             if abs(cur - target) < diff:
    #                 res, diff = cur, abs(cur - target)
    #     return res

    # 优化
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     nums.sort()
    #     res, diff = 0, float('inf')
    #     for i, num in enumerate(nums[:-2]):
    #         left, right = i + 1, len(nums) - 1
    #         if i > 0 and nums[i-1] == num:
    #             continue
    #         while left < right:
    #             cur = num + nums[left] + nums[right]
    #             if cur == target:
    #                 return cur
    #             elif cur < target:
    #                 # left += 1
    #                 # while left < right and nums[left] == nums[left-1]:  # 跳过重复的
    #                 #     left += 1
    #                 while left < right and nums[left] == nums[left + 1]:
    #                     left += 1
    #                 left += 1
    #             else:
    #                 # right -= 1
    #                 # while left < right and nums[right] == nums[right+1]:  # 跳过重复的
    #                 #     right -= 1
    #                 while left < right and nums[right] == nums[right - 1]:
    #                     right -= 1
    #                 right -= 1
    #             if abs(cur - target) < diff:
    #                 res, diff = cur, abs(cur - target)
    #     return res

    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     nums.sort()
    #     res, diff = 0, float('inf')
    #
    #     for i, num in enumerate(nums[:-2]):
    #         if i > 0 and num == nums[i-1]:
    #             continue
    #         left, right = i+1, len(nums)-1
    #         while left < right:
    #             cur = num + nums[left] + nums[right]
    #             if cur == target:
    #                 return cur
    #             elif cur > target:
    #                 while left < right and nums[right] == nums[right-1]:
    #                     right -= 1
    #                 right -= 1
    #             else:
    #                 while left < right and nums[left] == nums[left+1]:
    #                     left += 1
    #                 left += 1
    #             if abs(cur - target) < diff:
    #                 res, diff = cur, abs(cur - target)
    #     return res

    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     nums.sort()
    #     res, diff = 0, float('inf')
    #
    #     for i, num in enumerate(nums[:-2]):
    #         left, right = i+1, len(nums)-1
    #         while left < right:
    #             cur = num + nums[left] + nums[right]
    #             if cur == target:
    #                 return cur
    #             elif cur > target:
    #                 right -= 1
    #             else:
    #                 left += 1
    #             if abs(cur - target) < diff:
    #                 res, diff = cur, abs(cur - target)
    #     return res

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res, diff = 0, float('inf')
        for i, num in enumerate(nums[:-2]):
            if i > 1 and num == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                cur = num + nums[left] + nums[right]
                if cur == target:
                    return cur
                elif cur < target:
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                else:
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                if abs(cur-target) < diff:
                    res, diff = cur, abs(cur-target)
        return res


s = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(nums, target))

nums = [1,1,1,0]
target = 100
print(s.threeSumClosest(nums, target))
