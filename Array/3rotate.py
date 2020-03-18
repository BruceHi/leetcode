# def rotate(nums, k):
#     # temp = []
#     # if len(nums) > k:
#     #     for i in range(-k, 0):
#     #         temp.append(nums[i])
#     #
#     #     j = len(nums)
#     #     while j >= k:
#     #         nums[j - 1] = nums[j - 1 - k]
#     #         j -= 1
#     #
#     #     for i in range(0, k):
#     #         nums[i] = temp[i]
#
#     for i in range(k):
#         nums.insert(0, nums[-1])
#         nums.pop(-1)

# def reverse(nums):
#     for i in range(int(len(nums) / 2)):  # 循环不能全写完，否则又翻过来了
#         nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i],  nums[i]
#
#
# def rotate(nums, k):
#     reverse(nums)
#     reverse(nums[: k % len(nums)])
#     reverse(nums[k % len(nums):])


def rotate(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[::-1]
    # nums[:] = nums[k - 1::-1] + nums[: k - 1: -1]  # 前k个元素反转+剩余的元素反转。
    nums[:] = nums[:k][::-1] + nums[k:][::-1]


list1 = [1,2,3,4,5,6,7]
rotate(list1, 3)
print(list1)

list1 = [-1,-100,3,99]
rotate(list1, 2)
print(list1)

# list1 = [-1]
# rotate(list1, 2)
# print(list1)

list1 = [1, 2]
rotate(list1, 3)
print(list1)



list1 = [1, 2, 3]
rotate(list1, 4)
print(list1)