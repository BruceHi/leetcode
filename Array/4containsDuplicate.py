# def containsDuplicate(nums):
#
#     for i in range(len(nums) - 1):
#         for j in nums[i+1:]:
#             if nums[i] == j:
#                 return True
#
#     return False



def containsDuplicate(nums):
    # return False if len(set(nums)) == len(nums) or len(nums) == 0 else True
    # return True if len(set(nums)) != len(nums) else False
    return len(set(nums)) != len(nums)

# def containsDuplicate(nums):
#     for i in range(len(nums) - 1):
#         for j in range(len(nums) - 1 - i):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#
#     for i in range(len(nums) - 1):
#         if nums[i] == nums[i + 1]:
#             return True
#
#     return False


# def containsDuplicate(nums):
#     temp = set()
#     for i in nums:
#         if i in temp:
#             return True
#         else:
#             temp.add(i)
#     return False


list1 = [1,2,3,1]
print(containsDuplicate(list1))

list1 = [1,2,3,4]
print(containsDuplicate(list1))

list1 = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(list1))

list1 = [1]
print(containsDuplicate(list1))

list1 = []
print(containsDuplicate(list1))
