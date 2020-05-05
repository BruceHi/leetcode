# 原地排序，不稳定，O(nlgn)
import heapq


# 我的方法不太好
def heapsort(nums):
    heapq.heapify(nums)
    res = []
    for _ in range(len(nums)):
        res.append(heapq.heappop(nums))
    return res


nums = [4, 5, 3, 6, 11]
print(heapsort(nums))

nums = [8, 5, 3, 4, 11]

print(heapsort(nums))