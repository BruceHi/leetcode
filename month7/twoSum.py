from typing import List


class Solution:

    # # 双指针
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     left, right = 0, len(numbers) - 1
    #     while left < right:
    #         tmp = numbers[left] + numbers[right]
    #         if tmp < target:
    #             left += 1
    #         elif tmp > target:
    #             right -= 1
    #         else:
    #             return [left+1, right+1]

    # 二分查找
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     for i, num in enumerate(numbers[:-1]):
    #         left, right = i + 1, len(numbers) - 1
    #         while left <= right:  # 寻找确切数值，使用 = 号
    #             mid = left + right >> 1
    #             tmp = numbers[mid]
    #             if tmp == target - num:
    #                 return [i+1, mid+1]
    #             elif tmp < target - num:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp < target:
                left += 1
            elif tmp > target:
                right -= 1
            else:
                return [left+1, right+1]


s = Solution()
numbers = [2, 7, 11, 15]
target = 9
print(s.twoSum(numbers, target))

numbers = [2, 7, 11, 15]
target = 9
print(s.twoSum(numbers, target))