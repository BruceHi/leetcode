from typing import List


# class Solution:
#
#     # # 双指针
#     # def twoSum(self, numbers: List[int], target: int) -> List[int]:
#     #     left, right = 0, len(numbers) - 1
#     #     while left < right:
#     #         tmp = numbers[left] + numbers[right]
#     #         if tmp < target:
#     #             left += 1
#     #         elif tmp > target:
#     #             right -= 1
#     #         else:
#     #             return [left+1, right+1]
#
#     # 二分查找
#     # def twoSum(self, numbers: List[int], target: int) -> List[int]:
#     #     for i, num in enumerate(numbers[:-1]):
#     #         left, right = i + 1, len(numbers) - 1
#     #         while left <= right:  # 寻找确切数值，使用 = 号
#     #             mid = left + right >> 1
#     #             tmp = numbers[mid]
#     #             if tmp == target - num:
#     #                 return [i+1, mid+1]
#     #             elif tmp < target - num:
#     #                 left = mid + 1
#     #             else:
#     #                 right = mid - 1
#
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left, right = 0, len(numbers) - 1
#         while left < right:
#             tmp = numbers[left] + numbers[right]
#             if tmp < target:
#                 left += 1
#             elif tmp > target:
#                 right -= 1
#             else:
#                 return [left+1, right+1]

class Solution:

    def find_two(self, nums, target):
        nums.sort()
        res = []
        left, right = 0, len(nums) - 1
        while left < right:
            val = nums[left] + nums[right]
            if val < target:
                left += 1
            elif val > target:
                right -= 1
            else:
                res.append([nums[left], nums[right]])

                # 去重
                while left < right and nums[left+1] == nums[left]:
                    left += 1
                while left < right and nums[right-1] == nums[right]:
                    right -= 1
                left, right = left + 1, right - 1
        return res






s = Solution()
# numbers = [2, 7, 11, 15]
# target = 9
# print(s.twoSum(numbers, target))
#
# numbers = [2, 7, 11, 15]
# target = 9
# print(s.twoSum(numbers, target))

numbers = [2, 7, 11, 15, 1, 2, 8, 2, 8, 4, 5]
target = 9
print(s.find_two(numbers, target))

numbers = [5,9]
target = 9
print(s.find_two(numbers, target))