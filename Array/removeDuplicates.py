# 失败
# def removeDuplicates(nums):
#     for i in range(len(nums) - 2):
#         m = i + 1
#         for j in range(m, len(nums)):
#             if nums[i] == nums[j]:
#                 nums.remove(nums[j])
    # if nums[-1] == nums[-2]:
    #     nums.remove(nums[-1])


#  从排序数组中删除重复项
# def removeDuplicates(nums):
#     for i in range(len(nums) - 1):
#         for j in nums[i+1:]:
#             if nums[i] == j:
#                 nums.remove(j)   # 删除第一个与该值相等的匹配项,然后相对关系并没有发生改变。
#                 # nums.pop(i+1)  # 实际上删除后面的也完全可以。
#             else:
#                 break  # 用break时，表明只要下一个数字不相等，就退出该次循环。如果去掉的话，要白白遍历到头，因为说了是有序的。
#     return len(nums)
#
#
# list1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# print(removeDuplicates(list1))
# print(list1)
#


# 成功
# def removeDuplicates(nums):
#     i = 0
#     while i < len(nums) - 1:
#         if nums[i] == nums[i+1]:
#             nums.remove(nums[i])  # 去掉前面那个相同的，退出if，下次循环时，还是刚才的那个i.
#         else:  # 如果去掉了else就变成了死循环
#             i += 1
#     return len(nums)

# def removeDuplicates(nums):
#     if not nums:
#         return 0
#     slow = 0
#     for fast in range(1, len(nums)):
#         if nums[slow] != nums[fast]:
#             slow += 1
#             nums[slow] = nums[fast]
#     return slow + 1

from typing import List
# def removeDuplicates(nums: List[int]) -> int:
#     if not nums:
#         return 0
#     i = 0
#     for j in range(1, len(nums)):
#         if nums[i] != nums[j]:
#             i += 1
#             nums[i] = nums[j]
#     return i + 1


def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    i = 0
    for j, num in enumerate(nums):
        if num != nums[i]:
            i += 1
            nums[i] = num
    return i + 1



list1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(list1))
print(list1)
