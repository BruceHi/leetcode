# 移动0
# def moveZeroes(nums):
#     count = 0
#     i = 0
#     while i < len(nums):
#         if nums[i] == 0:
#             nums.remove(0)
#             count += 1
#             i -= 1
#         i += 1
#     nums.extend(0 for i in range(count))


# def moveZeroes(nums):

    # count = nums.count(0)
    #
    # # 正叙
    # for i in range(-len(nums), 0):
    #     if nums[i] == 0:
    #         nums.remove(nums[i])
    #
    # # 倒叙
    # for i in range(len(nums) - 1, -1, -1):
    #      if nums[i] == 0:
    #          # nums.remove(nums[i])
    #         nums.pop(i)  # 遍历到就删除，准确。
    #
    # nums.extend([0] * count)

###### 分界线 #####

# def moveZeroes(nums):
#
#     count = 0
#     # 倒叙并使用正数索引
#     for i in range(len(nums) - 1, -1, -1):
#         if not nums[i]:
#             nums.pop(i)  # 遍历到就删除，准确。
#             count += 1
#
#     nums.extend([0] * count)

# import collections
#
#
# def moveZeroes(nums):
#     count = collections.Counter(nums)[0]
#     # nums[:] = list(filter(lambda x: x, nums))
#     nums[:] = [x for x in nums if x]
#     nums.extend([0] * count)



# 双指针
# def moveZeroes(nums):
#     slow, fast = 0, 0
#     while fast < len(nums):
#         if nums[fast]:
#             nums[slow], nums[fast] = nums[fast], nums[slow]
#             slow += 1
#         fast += 1

# def moveZeroes(nums):
#     j = 0
#     for i in range(len(nums)):
#         if nums[i]:
#             nums[i], nums[j] = nums[j], nums[i]
#             j += 1


# def moveZeroes(nums):
#     i = 0
#     for j, val in enumerate(nums):
#         if val:
#             nums[i], nums[j] = val, nums[i]
#             i += 1

from typing import List

# def moveZeroes(nums: List[int]) -> None:
#     i = 0
#     for j, num in enumerate(nums):
#         if num:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1


def moveZeroes(nums: List[int]) -> None:
    i = 0
    for j, num in enumerate(nums):
        if num:
            nums[i], nums[j] = num, nums[i]
            i += 1


list1 = [1,1,0,3,0,12]
moveZeroes(list1)
print(list1)

list1 = [0,0,0,0,12]
moveZeroes(list1)
print(list1)

list1 = [0,1,0,3,12]
moveZeroes(list1)
print(list1)
