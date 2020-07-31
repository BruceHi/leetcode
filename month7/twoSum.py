from typing import List


class Solution:
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