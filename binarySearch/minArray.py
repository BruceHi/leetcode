# 剑指 offer 11. 旋转数组的最小数字
# 与 154. 寻找旋转排序数组中的最小值 II findMin 相同
from typing import List


class Solution:
    # def minArray(self, numbers: List[int]) -> int:
    #     for i, num in enumerate(numbers[:-1]):
    #         if num > numbers[i+1]:
    #             return numbers[i+1]
    #     return numbers[0]

    # 二分法
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = left + right >> 1
            tmp = numbers[mid]
            if tmp > numbers[right]:
                left = mid + 1
            elif tmp < numbers[right]:
                right = mid
            else:
                right -= 1
        return numbers[left]


s = Solution()
nums = [3,4,5,1,2]
print(s.minArray(nums))

nums = [2,2,2,0,1]
print(s.minArray(nums))

nums = [0, 1, 2, 3, 4]
print(s.minArray(nums))

nums = [3, 3, 1, 3]
print(s.minArray(nums))
