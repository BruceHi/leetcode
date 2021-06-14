# 137. 只出现一次的数字2
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。
from collections import Counter
from typing import List


class Solution:
    # 字典
    # def singleNumber(self, nums) -> int:
    #     count = Counter(nums)
    #     res, = [num for num in count if count[num] == 1]
    #     return res

    # 数学方法
    # def singleNumber(self, nums) -> int:
    #     return (3 * sum(set(nums)) - sum(nums)) // 2

    # def singleNumber(self, nums) -> int:
    #     count = Counter(nums)
    #     res, = [key for key, val in count.items() if val == 1]
    #     return res

    # def singleNumber(self, nums) -> int:
    #     return (sum(set(nums)) * 3 - sum(nums)) // 2

    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        a, = [x for x in count if count[x] == 1]
        return a


s = Solution()
nums = [2,2,3,2]
print(s.singleNumber(nums))

nums = [0,1,0,1,0,1,99]
print(s.singleNumber(nums))
