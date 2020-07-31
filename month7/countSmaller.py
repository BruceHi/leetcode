# 计算右侧小于当前元素的个数
from typing import List
from collections import OrderedDict
from collections import defaultdict
import bisect


class Solution:
    # # 错误版本
    # def countSmaller(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     res, dic = [0] * n, defaultdict(int)
    #
    #     for i in range(n-2, -1, -1):
    #         for j in range(i+1, n):
    #             if nums[j] < nums[i]:
    #                 tmp = dic[nums[j]]
    #                 res[i] = tmp + 1
    #                 dic[nums[i]] = tmp + 1
    #                 break
    #     return res

    def countSmaller(self, nums: List[int]) -> List[int]:
        res, sort_nums = [], []
        for num in nums[::-1]:
            idx = bisect.bisect_left(sort_nums, num)
            bisect.insort(sort_nums, num)
            res.append(idx)
        return res[::-1]


s = Solution()
nums = [5,2,6,1]
print(s.countSmaller(nums))

nums = [2,0,1]
print(s.countSmaller(nums))
