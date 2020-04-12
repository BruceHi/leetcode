# 二分查找
def binary_search(nums, item):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low+high) // 2
        guess = nums[mid]
        if guess == item:
            return mid
        if guess > item:  # 猜的数字大了
            high = mid - 1
        else:
            low = mid + 1


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
