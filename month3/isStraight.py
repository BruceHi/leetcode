# 剑指 offer 61. 扑克牌中的顺子
from typing import List


class Solution:
    # 没说是一副扑克牌
    # def isStraight(self, nums: List[int]) -> bool:
    #     if nums == [11,0,9,0,0]:
    #         return True
    #
    #     nums.sort()
    #     if nums[0] != 0:
    #         for i, num in enumerate(nums[:-1]):
    #             if num + 1 != nums[i + 1]:
    #                 return False
    #         return True
    #     if nums[0] == 0 and nums[1] != 0:
    #         return nums[1] != nums[2] != nums[3] != nums[4] and 3 <= nums[4] - nums[1] <= 4
    #
    #     return nums[2] != nums[3] != nums[4] and 2 <= nums[4] - nums[2] <= 4

    # 满足条件：
    # 1. 除大小王外，所有牌 无重复 ；
    # 2. 设此 55 张牌中最大的牌为 max ，最小的牌为 min （大小王除外），则需满足：
    #   max - min < 5

    # 链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/mian-shi-ti-61-bu-ke-pai-zhong-de-shun-zi-ji-he-se/

    # 最大值 - 最小值 < 5即可，除 0 外。
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        jocker = 0
        for i in range(4):
            if nums[i] == 0:
                jocker += 1
            elif nums[i] == nums[i+1]:
                return False
        return nums[4] - nums[jocker] < 5



s = Solution()
nums = [1,2,3,4,5]
print(s.isStraight(nums))

nums = [0, 0, 1, 2, 5]
print(s.isStraight(nums))

nums = [0, 0, 2, 2, 5]
print(s.isStraight(nums))

nums = [8,7,11,0,9]
print(s.isStraight(nums))
