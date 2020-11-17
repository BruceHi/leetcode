# 转变数组后最接近目标值的数组和
from typing import List
from bisect import bisect_left


class Solution:
    # def findBestValue(self, arr: List[int], target: int) -> int:
    #     n = len(arr)
    #     arr.sort()
    #     prefix = [0]
    #     for num in arr:
    #         prefix.append(prefix[-1] + num)
    #
    #     res, max_val, diff = 0, max(arr), target
    #
    #     for num in range(1, max_val+1):
    #         it = bisect_left(arr, num)  # 找到索引处
    #         cur = prefix[it] + (n - it) * num
    #         if abs(target - cur) < diff:
    #             res, diff = num, abs(target - cur)
    #     return res

    # def findBestValue(self, arr: List[int], target: int) -> int:
    #     n = len(arr)
    #     arr.sort()
    #     prefix = [0]
    #     for num in arr:
    #         prefix.append(prefix[-1] + num)
    #
    #     res, r, diff = 0, max(arr), target
    #     for num in range(1, r+1):
    #         it = bisect_left(arr, num)
    #         cur = prefix[it] + (n-it) * num
    #         if abs(target - cur) < diff:
    #             res, diff = num, abs(target - cur)
    #     return res

    # def findBestValue(self, arr: List[int], target: int) -> int:
    #     arr = sorted(arr)
    #     n = len(arr)
    #     diff = float('inf')
    #     res = 0
    #
    #     prefix, s = [], 0
    #     for num in arr:
    #         s += num
    #         prefix.append(s)
    #
    #     for num in range(0, arr[-1]+1):
    #         idx = bisect_left(arr, num)
    #         if not idx:
    #             tmp = n * num
    #         else:
    #             tmp = prefix[idx-1] + (n-idx) * num
    #         # tmp = sum(arr[:idx]) + (n-idx) * num
    #         if abs(tmp - target) < diff:
    #             diff = abs(tmp - target)
    #             res = num
    #     return res

    # def findBestValue(self, arr: List[int], target: int) -> int:
    #     n = len(arr)
    #     arr.sort()
    #     prefix = [0]  # 前缀和，并在前面补 [0]
    #     for num in arr:
    #         prefix.append(prefix[-1] + num)
    #
    #     res, diff = 0, float('inf')
    #     for num in range(0, arr[-1]+1):  # 枚举
    #         idx = bisect_left(arr, num)
    #         cur = prefix[idx] + (n-idx) * num
    #         if abs(cur - target) < diff:
    #             res, diff = num, abs(cur - target)
    #     return res

    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        arr.sort()
        pre = [0]
        for num in arr:
            pre.append(pre[-1] + num)

        res, diff = 0, float('inf')
        for num in range(arr[-1] + 1):
            i = bisect_left(arr, num)
            cur = abs(pre[i] + num * (n - i) - target)
            if cur < diff:
                res, diff = num, cur
        return res


s = Solution()
arr = [4,9,3]
target = 10
print(s.findBestValue(arr, target))

arr = [2,3,5]
target = 10
print(s.findBestValue(arr, target))

arr = [60864,25176,27249,21296,20204]
target = 56803
print(s.findBestValue(arr, target))
