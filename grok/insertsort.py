# 插入排序：原地排序，稳定
from typing import List


def insert_sort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        val = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > val:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = val
    return nums


nums = [7, 5, 9, 6, 2]
insert_sort(nums)
print(nums)

nums = []
insert_sort(nums)
print(nums)

nums = [1]
insert_sort(nums)
print(nums)

nums = [1, 4, 5, 6, 5, 6]
insert_sort(nums)
print(nums)