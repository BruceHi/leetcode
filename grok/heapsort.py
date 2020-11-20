# 堆排序
# 时间复杂度：最好，最坏，平均都是 O(nlogn)
# 原地排序，不稳定排序

# 大顶堆，正向排序。
# 与下面的相比，调整当前索引的正确位置，
# def heapify(nums, n, i):
#     left = 2*i + 1
#     right = 2*i + 2
#     largest = i
#
#     # 当前节点与左右节点较大的那个交换，但较大的节点也需要大于当前节点。
#     if left < n and nums[largest] < nums[left]:
#         largest = left
#     if right < n and nums[largest] < nums[right]:
#         largest = right
#
#     # 若是没有交换的，直接退出，否则继续交换该节点
#     if largest != i:
#         nums[i], nums[largest] = nums[largest], nums[i]
#         heapify(nums, n, largest)
#
#
# def heap_sort(nums):
#     n = len(nums)
#
#     # 建堆。从上到下堆化，只交换非叶子节点。
#     for i in reversed(range((n//2))):  # 来自 heapq.py 的用法。
#         heapify(nums, n, i)
#
#     # 排序。将堆的首尾交换，固定尾部。然后将索引为 0 的地方堆化，持续这个过程。
#     # 索引到 1，就结束了。
#     for i in range(n-1, 0, -1):
#         nums[0], nums[i] = nums[i], nums[0]
#         heapify(nums, i, 0)  # i 就是剩余要调整的堆的数量。
#     return nums

def heapify(nums, n, i):
    left = i*2 + 1
    right = i*2 + 2
    largest = i

    if left < n and nums[largest] < nums[left]:
        largest = left
    if right < n and nums[largest] < nums[right]:
        largest = right

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)


def heap_sort(nums):
    n = len(nums)
    # 从后往前堆化
    for i in reversed(range((n//2))):
        heapify(nums, n, i)

    for i in range(n-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
    return nums


nums = [7, 5, 9, 6, 2]
heap_sort(nums)
print(nums)

nums = []
heap_sort(nums)
print(nums)

nums = [1]
heap_sort(nums)
print(nums)

nums = [1, 4, 5, 6, 5, 6]
heap_sort(nums)
print(nums)
