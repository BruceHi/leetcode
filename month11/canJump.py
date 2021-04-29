# 55.跳跃游戏
# 判断你是否能够到达最后一个位置。
# 贪心
from typing import List


class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     n, right = len(nums), 0
    #     for i, num in enumerate(nums):
    #         if i <= right:
    #             right = max(right, i+num)
    #             if right >= n - 1:
    #                 return True
    #         else:
    #             return False
        # return True

    # def canJump(self, nums: List[int]) -> bool:
    #     jump = 0
    #     for i, num in enumerate(nums):
    #         if jump < i:
    #             return False
    #         jump = max(jump, i + num)
    #     return True


    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for i, num in enumerate(nums):
            if jump < i:
                return False
            jump = max(jump, i+num)
        return True


s = Solution()
print(s.canJump([2,3,1,1,4]))

print(s.canJump([3,2,1,0,4]))

print(s.canJump([3]))

print(s.canJump([0]))
