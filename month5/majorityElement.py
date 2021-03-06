# 众数
from typing import List
from collections import Counter


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     counts = Counter(nums)
    #     return max(counts.keys(), key=counts.get)  # 很是厉害,值得注意

    # def majorityElement(self, nums: List[int]) -> int:
    #     hash_map = {}
    #     for num in nums:
    #         hash_map[num] = hash_map.get(num, 0) + 1
    #         if hash_map[num] > len(nums) >> 1:
    #             return num

    # def majorityElement(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     res = count.most_common(1)
    #     return res[0][0]

    # def majorityElement(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     res, = [key for key in count if count[key] > len(nums) // 2]
    #     return res

    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count, key=count.get)


s = Solution()
nums = [3,2,3]
print(s.majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(s.majorityElement(nums))

#

