# 最小区间：与合并K个排序链表使用堆的思想一样
from typing import List
import heapq


class Solution:
    # def smallestRange(self, nums: List[List[int]]) -> List[int]:
    #     queue = []
    #     for i, num in enumerate(nums):
    #         heapq.heappush(queue, (num[0], i, 0))
    #
    #     start, end = queue[0][0], max(queue)[0]
    #     res, length = [start, end], end - start
    #     while True:
    #         _, x, y = heapq.heappop(queue)
    #         if y + 1 < len(nums[x]):
    #             heapq.heappush(queue, (nums[x][y+1], x, y+1))
    #         else:
    #             return res
    #         start, end = queue[0][0], max(queue)[0]
    #         if end - start < length:
    #             res = [start, end]
    #             length = end - start

    # # # 优化
    # def smallestRange(self, nums: List[List[int]]) -> List[int]:
    #     queue = [(num[0], i, 0) for i, num in enumerate(nums)]
    #     heapq.heapify(queue)
    #     start, end = queue[0][0], max(queue)[0]
    #     res, length = [start, end], end - start
    #
    #     while True:
    #         _, row, idx = heapq.heappop(queue)
    #         if idx + 1 < len(nums[row]):
    #             heapq.heappush(queue, (nums[row][idx+1], row, idx+1))
    #         else:
    #             break
    #         # start, end = queue[0][0], max(queue)[0]  # 不能全局求最大值
    #         start, end = queue[0][0], max(end, nums[row][idx+1])  # 这里比注释掉的那一行快大约 40倍。
    #         if end - start < length:
    #             res, length = [start, end], end - start
    #
    #     return res

    # 再优化，比之前快了大约 40倍。
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        queue = [(num[0], i, 0) for i, num in enumerate(nums)]
        heapq.heapify(queue)
        start, end = float('-inf'), float('inf')
        max_val = max(queue)[0]

        while True:
            min_val, row, idx = heapq.heappop(queue)
            if max_val - min_val < end - start:
                start, end = min_val, max_val
            if idx + 1 == len(nums[row]):
                break
            max_val = max(max_val, nums[row][idx+1])
            heapq.heappush(queue, (nums[row][idx+1], row, idx+1))

        return [start, end]


s = Solution()
nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print(s.smallestRange(nums))

nums = [[1,2,3],[1,2,3],[1,2,3]]
print(s.smallestRange(nums))