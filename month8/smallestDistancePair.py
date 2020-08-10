# 找出第 k 小的距离对长度
from typing import List
import heapq


class Solution:

    # # # 超时，时间复杂度是 O(n ^ 2)
    # def smallestDistancePair(self, nums: List[int], k: int) -> int:
    #     record = []
    #     n = len(nums)
    #     for i in range(n-1):
    #         for j in range(i+1, n):
    #             record.append(-abs(nums[i] - nums[j]))
    #
    #     queue = record[:k]
    #     heapq.heapify(queue)
    #     for num in record[k:]:
    #         heapq.heappushpop(queue, num)
    #     return -queue[0]

    # # # 超时，时间复杂度是 O(n ^ 2)
    # def smallestDistancePair(self, nums: List[int], k: int) -> int:
    #     queue = []
    #     n = len(nums)
    #     for i in range(n-1):
    #         for j in range(i+1, n):
    #             queue.append(abs(nums[i] - nums[j]))
    #     heapq.heapify(queue)
    #
    #     for _ in range(k-1):
    #         heapq.heappop(queue)
    #     return heapq.heappop(queue)

    # 太难了，以后要再看一下
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:  # 枚举所有可能出现的距离的绝对值长度
            mid = left + right >> 1
            count, start = 0, 0
            # 统计的是小于或等于mid 的对数
            for i, num in enumerate(nums):
                while num - nums[start] > mid:
                    start += 1
                count += i - start
            if count < k:
                left = mid + 1
            else:
                right = mid
        return right





s = Solution()
nums = [1,3,1]
k = 1
print(s.smallestDistancePair(nums, k))


nums = [1,3,4, 1]
k = 6
print(s.smallestDistancePair(nums, k))

