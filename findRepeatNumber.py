# 剑指 offer 03.数组中重复的数字
from typing import List
from collections import Counter


class Solution:
    # 词频
    # def findRepeatNumber(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     return [key for key in count if count[key] > 1][0]

    def findRepeatNumber(self, nums: List[int]) -> int:
        record = set()
        for num in nums:
            if num in record:
                return num
            record.add(num)


s = Solution()
nums = [2, 3, 1, 0, 2, 5, 3]
print(s.findRepeatNumber(nums))
