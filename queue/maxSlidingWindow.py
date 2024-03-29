# 滑动窗口最大值，需要自己进行移动
from typing import List
from collections import deque
import heapq


class Solution:

    # # 暴力法都不怎么会,
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if k >= len(nums):
    #         return [max(nums)]
    #     # res = []
    #     # for i in range(len(nums)-k+1):  # 需要多少个滑动窗口
    #     #     res.append(max(nums[i:i+k]))
    #     # return res
    #     return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]

    # # 双端队列
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if k >= len(nums):
    #         return [max(nums)]
    #     queue, res = deque(), []
    #     for i, v in enumerate(nums):
    #
    #         # 清理
    #         if i > 0 and v > queue[0]:  # 直接比较最左边，看是否可以删完。
    #             queue.clear()
    #         else:  # 否则一个一个删。
    #             while i > 0 and v > queue[-1]:  # i 的判定不能少
    #                 queue.pop()
    #
    #         queue.append(v)  # 添加元素
    #
    #         # 不能移动到清理的前面，这种情况 nums = [1, -1]，k = 1 就不行。
    #         if i >= k and nums[i-k] == queue[0]:  # 移动窗口（或更新到正常窗口）
    #             queue.popleft()
    #
    #         if i >= k-1:
    #             res.append(queue[0])
    #     return res

    # 双端队列：对上面做出小改动，包括移动窗口放前面，清理要再加一个判断条件。
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if k >= len(nums):
    #         return [max(nums)]
    #     queue, res = deque(), []
    #     for i, v in enumerate(nums):
    #
    #         # nums = [1, -1]，k = 1
    #         if i >= k and nums[i - k] == queue[0]:  # 移动窗口（或更新到正常窗口）
    #             queue.popleft()
    #
    #         # 清理
    #         if len(queue) > 0:  # 队列里面不是空的，才要考虑要不要清零。确实，每次要这个判定，还是相当费时的。
    #             if v > queue[0]:  # 由于有前面的语句。i == 0时，queue 肯定就是空的，所以去掉 i 的判定。
    #                 queue.clear()
    #             else:  # 否则一个一个删。
    #                 while v > queue[-1]:
    #                     queue.pop()
    #
    #         queue.append(v)  # 添加元素
    #
    #         if i >= k - 1:
    #             res.append(queue[0])
    #     return res

    # # 双端队列一点小改动
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if k >= len(nums):
    #         return [max(nums)]
    #     queue, res = deque(), []
    #     for i, v in enumerate(nums):
    #
    #         if i >= k and nums[i - k] == queue[0]:  # 移动窗口（或更新到正常窗口）
    #             queue.popleft()
    #
    #         # 清理，注意不能是等号，nums = [-7,-8,7,5,7,1,6,0]，k = 4，由于查看的是元素，可能上面会误删。
    #         while queue and v > queue[-1]:
    #             queue.pop()
    #
    #         queue.append(v)  # 添加元素
    #
    #         if i >= k - 1:
    #             res.append(queue[0])
    #     return res

    # # 队列里面存的值是索引值，而非数据。上面存的都是数据。太慢了，412ms
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if k >= len(nums):
    #         return [max(nums)]
    #     queue, res = deque(), []
    #     for i, v in enumerate(nums):
    #
    #         if i >= k and queue[0] == i - k:  # 移动窗口（或更新到正常窗口）
    #             queue.popleft()
    #
    #         while queue and v >= nums[queue[-1]]:  # 清理，注意可以包括等号
    #             queue.pop()
    #
    #         queue.append(i)  # 添加元素的索引
    #
    #         if i >= k - 1:
    #             res.append(nums[queue[0]])
    #     return res

    # 更慢
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if len(nums) <= k:
    #         return [max(nums)]
    #
    #     res, queue = [], deque()
    #     for i, num in enumerate(nums):
    #         if i >= k and queue[0] == i - k:
    #             queue.popleft()
    #
    #         if queue and num > nums[queue[0]]:
    #             queue.clear()
    #         else:
    #             while queue and num >= nums[queue[-1]]:  # 判断 queue 必须要用，因为后面要用到 queue
    #                 queue.pop()
    #
    #         queue.append(i)
    #         if i >= k - 1:
    #             res.append(nums[queue[0]])
    #     return res

    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if len(nums) <= k:
    #         return [max(nums)]
    #     queue = deque()
    #     res = []
    #     for i, num in enumerate(nums):
    #
    #         if i >= k and queue[0] == i - k:
    #             queue.popleft()
    #
    #         while queue and num >= nums[queue[-1]]:
    #             queue.pop()
    #
    #         queue.append(i)
    #
    #         if i >= k-1:
    #             res.append(nums[queue[0]])
    #
    #     return res

    # 战胜 93%
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     res = []
    #     queue = deque()
    #     for i, num in enumerate(nums):
    #         if i >= k and i - queue[0] == k:  # 比较索引
    #             queue.popleft()
    #
    #         while queue and num >= nums[queue[-1]]:  # 比较值
    #             queue.pop()
    #
    #         queue.append(i)
    #         if i >= k-1:
    #             res.append(nums[queue[0]])
    #     return res

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        for i, num in enumerate(nums):
            if queue and i - queue[0] == k:
                queue.popleft()
            while queue and num >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i >= k-1:
                res.append(nums[queue[0]])
        return res


s = Solution()
nums = [-7,-8,7,5,7,1,6,0]
k = 4
print(s.maxSlidingWindow(nums, k))


nums = [0, 1, 4, 2, 3]
k = 2
print(s.maxSlidingWindow(nums, k))


nums = [1, -1]
k = 1
print(s.maxSlidingWindow(nums, k))


nums = [1,3,1,2,0,5]
k = 3
print(s.maxSlidingWindow(nums, k))


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(s.maxSlidingWindow(nums, k))
print('😘')

# 结果
# [7, 7, 7, 7, 7]
# [1, 4, 4, 3]
# [1, -1]
# [3, 3, 2, 5]
# [3, 3, 5, 5, 6, 7]
# 😘
