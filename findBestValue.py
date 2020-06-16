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

    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        arr.sort()
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        res, r, diff = 0, max(arr), target
        for num in range(1, r+1):
            it = bisect_left(arr, num)
            cur = prefix[it] + (n-it) * num
            if abs(target - cur) < diff:
                res, diff = num, abs(target - cur)
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
