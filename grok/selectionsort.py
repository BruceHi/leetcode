# 选择排序 不稳定、原地算法。O(n^2)
def find_smallest(arr):
    small = float('inf')
    small_index = None
    for i, v in enumerate(arr):
        if v < small:
            small = v
            small_index = i
    return small_index


# def select_sort(arr):  # array的缩写
#     for i in range(len(arr)):
#         # j = find_smallest(arr[i:])  # 这样写的话，返回值可能小于当前的i
#         j = i + find_smallest(arr[i:])
#         arr[i], arr[j] = arr[j], arr[i]

def select_sort(arr):  # 当 nums 为空的时候，什么都不执行。没有返回值，相当于返回值是None.
    for i in range(len(arr)):
        min_index = i
        min_val = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


nums = [7, 5, 9, 6, 2]
select_sort(nums)
print(select_sort(nums))
print(nums)

nums = []
print(select_sort(nums))
print(nums)


