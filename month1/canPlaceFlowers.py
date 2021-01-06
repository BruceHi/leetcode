# 605. 种花问题
from typing import List


class Solution:
    # 首尾添加一个 0，不用考虑边界条件
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        nums = [0] + flowerbed + [0]
        for i in range(1, len(nums)-1):
            if nums[i-1:i+2] == [0] * 3:
                nums[i] = 1
                n -= 1
        return n <= 0


s = Solution()
flowerbed = [1,0,0,0,1]
n = 1
print(s.canPlaceFlowers(flowerbed, n))

flowerbed = [1,0,0,0,1]
n = 2
print(s.canPlaceFlowers(flowerbed, n))
