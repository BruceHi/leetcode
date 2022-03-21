from typing import List


class Solution:
    # def minimumDifference(self, nums: List[int], k: int) -> int:
    #     if k == 1:
    #         return 0
    #     nums.sort()
    #     res = []
    #     for i, num in enumerate(nums[:-1]):
    #         res.append(nums[i+1]-num)
    #     print(max(nums), min(nums), max(nums)-min(nums))
    #     return min(res)

    # def minimumDifference(self, nums: List[int], k: int) -> int:
    #     if k == 1:
    #         return 0
    #     res = float('inf')
    #     nums.sort()
    #     for i in range(len(nums)-k+1):
    #         res = min(res, nums[i+k-1]-nums[i])
    #     return res
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # if k == 1:
        #     return 0
        nums.sort()
        res = float('inf')
        for i in range(len(nums)-k+1):
            res = min(res, nums[i+k-1]-nums[i])
        return res


s = Solution()
nums = [90]
k = 1
print(s.minimumDifference(nums, k))

nums = [9,4,1,7]
k = 2
print(s.minimumDifference(nums, k))

# 74560
nums = [87063,61094,44530,21297,95857,93551,9918]
k = 6
print(s.minimumDifference(nums, k))
