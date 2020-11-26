# 448. 找到所有数组中消失的数字
# # 原地修改，标记负数
# # 1 标记到位置 0
from typing import List


class Solution:
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     return list(set(range(1, len(nums)+1)) - set(nums))

    # # 原地修改，又是这种不使用额外空间的方法，标记负数
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     for num in nums:
    #         idx = abs(num) - 1
    #         if nums[idx] > 0:
    #             nums[idx] *= -1
    #
    #     res = []
    #     for i in range(1, n+1):
    #         if nums[i-1] > 0:
    #             res.append(i)
    #     return res

    # 快
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     return list({x for x in range(1, len(nums)+1)} - set(nums))

    # 慢
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list({x for x in range(1, len(nums)+1)} - {x for x in nums})


s = Solution()
nums = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums))
