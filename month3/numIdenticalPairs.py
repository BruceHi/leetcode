# 1512.好数对的个数
from typing import List
from collections import defaultdict, Counter


class Solution:
    # def numIdenticalPairs(self, nums: List[int]) -> int:
    #     dic = defaultdict(int)
    #     res = 0
    #     for num in nums:
    #         res += dic[num]
    #         dic[num] += 1
    #     return res

    # 使用组合公式
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sum(v*(v-1)//2 for v in counter.values())


s = Solution()
nums = [1,2,3,1,1,3]
print(s.numIdenticalPairs(nums))

nums = [1,1,1,1]
print(s.numIdenticalPairs(nums))

nums = [1,2,3]
print(s.numIdenticalPairs(nums))

nums = [1]
print(s.numIdenticalPairs(nums))