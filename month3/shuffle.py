# 1470.重新排列数组
from typing import List


class Solution:
    # def shuffle(self, nums: List[int], n: int) -> List[int]:
    #     res = []
    #     i, j = 0, n
    #     while i < n and j < 2*n:
    #         res.extend([nums[i], nums[j]])
    #         i, j = i+1, j+1
    #     return res

    # def shuffle(self, nums: List[int], n: int) -> List[int]:
    #     res = []
    #     for i in range(n):
    #         res.extend([nums[i], nums[i+n]])
    #     return res

    # 切片
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums


s = Solution()
nums = [2,5,1,3,4,7]
n = 3
print(s.shuffle(nums, n))

nums = [1,2,3,4,4,3,2,1]
n = 4
print(s.shuffle(nums, n))

nums = [1,1,2,2]
n = 2
print(s.shuffle(nums, n))
