# 229. 求众数2
from typing import List
from collections import Counter


class Solution:
    # def majorityElement(self, nums: List[int]) -> List[int]:
    #     count = Counter(nums)
    #     res = []
    #     for k, v in count.items():
    #         if v > len(nums) // 3:
    #             res.append(k)
    #     return res

    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [k for k, v in count.items() if v > len(nums)//3]


s = Solution()
nums = [3,2,3]
print(s.majorityElement(nums))

nums = [1]
print(s.majorityElement(nums))

nums = [1,1,1,3,3,2,2,2]
print(s.majorityElement(nums))
