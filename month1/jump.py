# 45. 跳跃游戏2
from typing import List


class Solution:

    # 从后往前贪心，时间复杂度为 O(n^2)，超时
    # def jump(self, nums: List[int]) -> int:
    #     n = len(nums) - 1
    #     res = 0
    #     while n > 0:
    #         for i in range(n):
    #             if i + nums[i] >= n:
    #                 n = i
    #                 res += 1
    #                 break
    #     return res

    # # 正向贪心，时间复杂度为 O(n)
    # def jump(self, nums: List[int]) -> int:
    #     res = 0
    #     end = 0
    #     max_pos = 0
    #     for i, num in enumerate(nums[:-1]):
    #         if max_pos >= i:
    #             max_pos = max(max_pos, num + i)  # 下次位置
    #             if i == end:
    #                 end = max_pos
    #                 res += 1
    #     return res

    # 不要判断也行
    def jump(self, nums: List[int]) -> int:
        res = 0
        end = 0
        max_pos = 0
        for i, num in enumerate(nums[:-1]):
            max_pos = max(max_pos, num + i)  # 下次位置
            if i == end:
                end = max_pos
                res += 1
        return res


s = Solution()
nums = [2,3,1,1,4]
print(s.jump(nums))

nums = [0]
print(s.jump(nums))

nums = [2, 0, 1]
print(s.jump(nums))
