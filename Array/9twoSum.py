# def twoSum(nums, target):
#
#     i = 0
#     while i < len(nums) - 1:
#         try:
#             position = nums.index(target - nums[i], i + 1)
#             return [i, position]
#         except:
#             i += 1

# # 暴力搜索
# def twoSum(nums, target):
#     for i in range(len(nums) - 1):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# hash 表
# def twoSum(nums, target):
#
#     hashmap = {}
#     for i in range(len(nums)):
#         temp = target - nums[i]
#         if temp in hashmap:
#             return hashmap[temp], i
#         else:
#             hashmap[nums[i]] = i

# def twoSum(nums, target):
#     hash_map = {}
#     for i, val in enumerate(nums):
#         if target-val in hash_map:
#             return [hash_map[target-val], i]
#         hash_map[val] = i

def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target-num], i]
        hash_map[num] = i


list1 = [3,2,4]
target = 6
print(twoSum(list1, target))


list1 = [2, 7, 11, 15]
target = 9
print(twoSum(list1, target))



