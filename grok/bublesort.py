# 冒泡排序
# def bubulesort(nums):
#     n = len(nums)
#     for j in range(n-1):  # 总共比较 n-1 次
#         for i in range(n-1-j):  # 每次比较的元素个数
#             if nums[i] > nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]


# 冒泡排序, 改进
def bubule_sort(nums):
    n = len(nums)
    for j in range(n-1):
        swap = False
        for i in range(n-1-j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swap = True
        if not swap:
            break


nums = [7, 5, 9, 6, 2]
bubule_sort(nums)
print(nums)

nums = []
bubule_sort(nums)
print(nums)

nums = [1]
bubule_sort(nums)
print(nums)

nums = [1, 4, 5, 6, 5, 6]
bubule_sort(nums)
print(nums)