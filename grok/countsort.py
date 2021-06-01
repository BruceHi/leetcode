# 计数排序，原始解法
# def count_sort(nums):
#     if not nums:
#         return []
#     max_num = max(nums)
#     count = [0] * (max_num+1)
#     for num in nums:
#         count[num] += 1
#     res = []
#     for num in range(max_num+1):
#         while count[num] > 0:  # 针对重复的数字进行多次记录。比如排序 [2, 5, 6, 5]，5 要记录 2 次。
#             res.append(num)
#             count[num] -= 1
#     return res

# 改进：缩短所需空间
# def count_sort(nums):
#     if not nums:
#         return []
#     max_num, min_num = max(nums), min(nums)
#     count = [0] * (max_num-min_num+1)
#
#     for num in nums:
#         count[num-min_num] += 1
#
#     res = []
#     for i, num in enumerate(count):
#         while num > 0:
#             res.append(i+min_num)
#             num -= 1
#     return res

def count_sort(nums):
    if not nums:
        return []
    max_v = max(nums)
    count = [0] * (max_v+1)

    for num in nums:
        count[num] += 1

    res = []
    for i in range(max_v+1):
        while count[i]:  # 减到 0 时停止循环。
            res.append(i)
            count[i] -= 1
    return res


nums = [7, 5, 9, 6, 2]
print(count_sort(nums))

nums = []
print(count_sort(nums))

nums = [1]
print(count_sort(nums))

nums = [1, 4, 5, 6, 5, 6]
print(count_sort(nums))
