# 1480. 一维数组的动态和
from typing import List


class Solution:
    # def runningSum(self, nums: List[int]) -> List[int]:
    #     res = [0]
    #     for num in nums:
    #         res.append(res[-1] + num)
    #     return res[1:]

    # # 修改 nums 的值，这样是错误的，边运行边解包
    # def runningSum(self, nums: List[int]) -> List[int]:
    #     # 这样错误，在下次使用之前，已经解包了
    #     for i, num in enumerate(nums[:-1]):
    #         nums[i+1] += num
    #     return nums

    # 修改 nums 的值
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums


s = Solution()
nums = [1,2,3,4]
print(s.runningSum(nums))

nums = [1,1,1,1,1]
print(s.runningSum(nums))

nums = [3,1,2,10,1]
print(s.runningSum(nums))
