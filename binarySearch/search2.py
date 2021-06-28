#  33.搜索旋转排序数组, 要求时间复杂度为 O(log n)
# 数组中的值互不相同
from typing import List


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #         left, right = 0, len(nums) - 1
    #         while left <= right:
    #             mid = left + right >> 1
    #             tmp = nums[mid]
    #             if tmp == target:
    #                 return mid
    #             if nums[0] <= tmp:
    #                 if nums[0] <= target < tmp:
    #                     right = mid - 1
    #                 else:
    #                     left = mid + 1
    #             else:
    #                 if tmp < target <= nums[-1]:
    #                     left = mid + 1
    #                 else:
    #                     right = mid - 1
    #         return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = left + right >> 1
    #         if nums[mid] == target:
    #             return mid
    #         if nums[mid] >= nums[left]:
    #             if target >= nums[left]:
    #                 if nums[mid] < target:
    #                     left = mid + 1
    #                 else:
    #                     right = mid - 1
    #             else:
    #                 left = mid + 1
    #         else:
    #             if target <= nums[right]:
    #                 if nums[mid] < target:
    #                     left = mid + 1
    #                 else:
    #                     right = mid - 1
    #             else:
    #                 right = mid - 1
    #     return -1


    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = left + right >> 1
    #         if nums[mid] == target:
    #             return mid
    #         if nums[mid] >= nums[left]:  # = 不能省略
    #             if nums[left] <= target < nums[mid]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1
    #         else:
    #             if nums[mid] < target <= nums[right]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #     return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = left + right >> 1
    #         if nums[mid] == target:
    #             return mid
    #         if nums[mid] >= nums[left]:  # = 不能省略
    #             if nums[left] <= target < nums[mid]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1
    #         else:
    #             if nums[mid] < target <= nums[right]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #     return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = left + right >> 1
    #         if nums[mid] == target:
    #             return mid
    #         if nums[mid] >= nums[left]:
    #             if nums[left] <= target < nums[mid]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1
    #         else:
    #             if nums[mid] < target <= nums[right]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #     return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + right >> 1
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right -= 1
                else:
                    left += 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(s.search(nums, target))

nums = [4,5,6,7,0,1,2]
target = 3
print(s.search(nums, target))

nums = [0,1,2,4,5,6,7]
target = 0
print(s.search(nums, target))

# nums = []
# target = 0
# print(s.search(nums, target))

nums = [1, 3]
target = 3
print(s.search(nums, target))

nums = [4,5,6,7,8,1,2,3]
target = 8
print(s.search(nums, target))

nums = [5,1,3]
target = 3
print(s.search(nums, target))

nums = [3, 1]
target = 1
print(s.search(nums, target))
