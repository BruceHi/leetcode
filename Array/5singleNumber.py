# 只出现一次的数字


#  数学方法
# def singleNumber(nums):
#
#     return 2 * sum(set(nums)) - sum(nums)



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
