# 697.数组的度
from typing import List
from collections import Counter


class Solution:
    # def findShortestSubArray(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     max_count = count.most_common(1)[0][1]
    #
    #     res = float('inf')
    #     for key, val in count.items():
    #         if val == max_count:
    #             left, right = nums.index(key), len(nums) - nums[::-1].index(key)
    #             print('a', right)
    #             res = min(res, right-left)
    #     return res
    #     # if count[1]
    #     # print(max_val)

    # 最后出现索引记录方法很巧妙
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        left, right = {}, {}
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
        res = len(nums)
        degree = max(count.values())
        for i, val in count.items():
            if val == degree:
                res = min(res, right[i]-left[i]+1)
        return res


s = Solution()
nums = [1, 2, 2, 3, 1]
print(s.findShortestSubArray(nums))

nums = [1,2,2,3,1,4,2]
print(s.findShortestSubArray(nums))
