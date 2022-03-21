# 376. 摆动序列
from typing import List


class Solution:
    # 贪心法
    # 去重，求所有的峰和谷的数量，即最大值
    # def wiggleMaxLength(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #
    #     new = []
    #     for num in nums:
    #         if not new or new[-1] != num:
    #             new.append(num)
    #     if len(new) == 1:
    #         return 1
    #
    #     res = 2
    #     n = len(new)
    #     for i in range(1, n-1):
    #         if new[i-1] < new[i] > new[i+1] or new[i-1] > new[i] < new[i+1]:
    #             res += 1
    #     return res

    def wiggleMaxLength(self, nums: List[int]) -> int:
        new = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != new[-1]:
                new.append(nums[i])

        n = len(new)
        if n == 1:
            return 1

        res = 2
        for i in range(1, n-1):
            if new[i-1] < new[i] > new[i+1] or new[i-1] > new[i] < new[i+1]:
                res += 1
        return res


s = Solution()
nums = [1,7,4,9,2,5]
print(s.wiggleMaxLength(nums))

nums = [1,17,5,10,13,15,10,5,16,8]
print(s.wiggleMaxLength(nums))

nums = [1,2,3,4,5,6,7,8,9]
print(s.wiggleMaxLength(nums))

nums = [1, 4, 2]
print(s.wiggleMaxLength(nums))

nums = [1]
print(s.wiggleMaxLength(nums))

nums = [1, 1]
print(s.wiggleMaxLength(nums))

nums = [1, 2, 2, 1]
print(s.wiggleMaxLength(nums))

nums = [3,3,3,2,5]
print(s.wiggleMaxLength(nums))
