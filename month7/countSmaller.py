# 计算右侧小于当前元素的个数，参考答案使用归并排序，以后再说这个
from typing import List
from collections import OrderedDict
from collections import defaultdict
import bisect


class Solution:

    # def countSmaller(self, nums: List[int]) -> List[int]:
    #     res, sort_nums = [], []
    #     for num in nums[::-1]:
    #         idx = bisect.bisect_left(sort_nums, num)
    #         bisect.insort(sort_nums, num)
    #         res.append(idx)
    #     return res[::-1]

    # 暴力法超时，时间复杂度是 O(n^2)，不管哪种优化方法都是要扫描一下数组的，时间复杂度至少是 O(n)
    # 就看得出结果能优化成 O(1)，还是 O(log n)
    # def countSmaller(self, nums: List[int]) -> List[int]:
    #     if not nums:
    #         return []
    #
    #     res = []
    #     for i, num in enumerate(nums[:-1]):
    #         count = 0
    #         for j in range(i+1, len(nums)):
    #             if nums[j] < num:
    #                 count += 1
    #         res.append(count)
    #     res.append(0)
    #     return res

    def countSmaller(self, nums: List[int]) -> List[int]:
        res, sort_nums = [], []
        for num in nums[::-1]:
            idx = bisect.bisect_left(sort_nums, num)
            # bisect.insort(sort_nums, num)
            sort_nums = sort_nums[:idx] + [num] + sort_nums[idx:]
            res.append(idx)
        return res[::-1]



s = Solution()
nums = [5,2,6,1]
print(s.countSmaller(nums))

nums = [2,0,1]
print(s.countSmaller(nums))  # [2, 0, 0]
