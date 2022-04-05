# 数组中的第K个最大元素
from typing import List
import heapq
from random import randint

class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # return heapq.nlargest(k, nums)[k-1]
    #     return sorted(nums, reverse=True)[k-1]

    # 快排的思想
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     self.partition(nums, 0, len(nums)-1, k)
    #     return nums[k-1]
    #
    # def partition(self, nums, left, right, k):
    #     if left > right:
    #         return
    #     pivot, i = nums[right], left
    #     for j in range(left, right):
    #         if nums[j] > pivot:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             i += 1
    #     nums[i], nums[right] = pivot, nums[i]
    #     if i+1 < k:
    #         return self.partition(nums, i+1, right, k)
    #     elif i+1 > k:
    #         return self.partition(nums, left, i-1, k)
    #     return i

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     left, right = 0, n-1
    #     while True:
    #         p = self.partition(nums, left, right)
    #         if p+1 == k:
    #             return nums[p]
    #         elif k > p+1:
    #             left = p + 1
    #         else:
    #             right = p - 1
    #
    # def partition(self, nums, left, right):
    #     ran_idx = randint(left, right)  # 引入随机基准
    #     nums[right], nums[ran_idx] = nums[ran_idx], nums[right]
    #
    #     pivot, i = nums[right], left
    #     for j in range(left, right):
    #         if nums[j] > pivot:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             i += 1
    #     nums[i], nums[right] = pivot, nums[i]
    #     return i

    # 维护一个大小为 k 的小顶堆。
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     queue = nums[:k]
    #     heapq.heapify(queue)
    #     for num in nums[k:]:
    #         heapq.heappushpop(queue, num)
    #     return queue[0]
    #
    # # 数组中的第 K 个最小元素，使用堆
    # def findKthSmallest(self, nums: List[int], k: int) -> int:
    #     queue = nums[:]
    #     heapq.heapify(queue)
    #     for _ in range(k-1):
    #         heapq.heappop(queue)
    #     return queue[0]

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     queue = nums[:k]
    #     heapq.heapify(queue)
    #     for num in nums[k:]:
    #         if num > queue[0]:  # 加上这一句，不用每次都进行堆排序。
    #             heapq.heappushpop(queue, num)
    #     return queue[0]

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #
    #     def partition(nums, left, right):
    #         ran_idx = randint(left, right)
    #         nums[ran_idx], nums[right] = nums[right], nums[ran_idx]
    #
    #         pivot, i = nums[right], left
    #         for j in range(left, right):
    #             if nums[j] > pivot:
    #                 nums[i], nums[j] = nums[j], nums[i]
    #                 i += 1
    #         nums[i], nums[right] = pivot, nums[i]
    #         return i
    #
    #     left, right = 0, len(nums) - 1
    #     while True:
    #         p = partition(nums, left, right)
    #         if p + 1 == k:
    #             return nums[p]
    #         if p + 1 > k:
    #             right = p - 1
    #         else:
    #             left = p + 1

    def findKthSmallest(self, nums: List[int], k: int) -> int:
        arr = [-num for num in nums]
        queue = arr[:k]
        heapq.heapify(queue)
        for num in arr[k:]:
            if num > queue[0]:
                heapq.heappushpop(queue, num)
        return -queue[0]

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     queue = nums[:k]
    #     heapq.heapify(queue)
    #     for num in nums[k:]:
    #         if num > queue[0]:
    #             heapq.heapreplace(queue, num)
    #     return queue[0]

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     queue = nums[:k]
    #     heapq.heapify(queue)
    #     for num in nums[k:]:
    #         heapq.heappushpop(queue, num)  # 内部有判定机制 num 与 queue[0] 的比较
    #     return queue[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        # for _ in range(k-1):
        #     heapq.heappop(nums)
        # return nums[0]

        new = nums[:k]
        heapq.heapify(new)
        for num in nums[k:]:
            heapq.heappushpop(new, num)
        return new[0]


s = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(s.findKthLargest(nums, k))

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(s.findKthLargest(nums, k))


nums = [3,2,1,5,6,4]
k = 2
print(s.findKthSmallest(nums, k))