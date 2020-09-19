# 只出现一次的数字

## 在原有数组上删除，难度太大
# def singleNumber(nums):
#     i = 0
#     while i < len(nums) - 1:
#         for j in nums[i + 1:]:
#             if nums[i] == j:
#                 nums.remove(nums[i])
#                 nums.remove(j)
#                 i = 0
#                 break
#         if i == 0:
#             break
#         i = 1
#      return nus[0]
#
#  数学方法
# def singleNumber(nums):
#
#     return 2 * sum(set(nums)) - sum(nums)


# 列表操作
# def singleNumber(nums):
#
#     new_list = []
#     for i in nums:
#         if i not in new_list:
#             new_list.append(i)
#         else:
#             new_list.remove(i)
#     return new_list[0]

# 异或方法
# def singleNumber(nums):
#     result = 0
#     for i in nums:
#         result ^= i
#     return result

# hash 表
# def singleNumber(nums):
#     hash_table = {}
#     for i in nums:
#         if hash_table.get(i) is not None:
#             hash_table[i] = 1
#         else:
#             hash_table[i] = 0  # 首次出现赋值为0，再次出现赋值为1
#
#     for key, value in hash_table.items():
#         if value == 0:  # 返回值为0的键
#             return key

# 官方题解
# def singleNumber(nums):
#     hash_table = {}
#     for i in nums:
#         try:
#             hash_table.pop(i)
#         except:
#             hash_table[i] = i
#
#     return hash_table.popitem()[0]


# 集合
# def singleNumber(nums):
#     temp = set()
#     for i in nums:
#         if i in temp:
#             temp.remove(i)
#         else:
#             temp.add(i)
#     return temp.pop()


from typing import List


def singleNumber(nums: List[int]) -> int:
    res = nums[0]
    for num in nums[1:]:
        res ^= num
    return res


list1 = [1,3,1,-1,3]
print(singleNumber(list1))

list1 = [1,0,1]
print(singleNumber(list1))

list1 = [2,2,1]
print(singleNumber(list1))

list1 = [4,1,2,1,2]
print(singleNumber(list1))