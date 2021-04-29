from typing import List
from collections import defaultdict

class Solution:
    # 暴力法果然超时
    # def purchasePlans(self, nums: List[int], target: int) -> int:
    #     res = 0
    #     for i, num in enumerate(nums[:-1]):
    #         for j in range(i+1, len(nums)):
    #             if num + nums[j] <= target:
    #                 res += 1
    #     return res % 1000000007


    # def purchasePlans(self, nums: List[int], target: int) -> int:
    #     nums.sort()
    #     n = len(nums)
    #     res = 0
    #     left = 0
    #     while left < n-1 or nums[left] >= target:
    #         # val = nums[left]
    #         for i in range(left+1, n):
    #             if nums[left] + nums[i] <= target:
    #                 res += 1
    #             else:
    #                 break
    #         left += 1
    #     return res % 1000000007

    # 超时了
    # def purchasePlans(self, nums: List[int], target: int) -> int:
    #     nums.sort()
    #     n = len(nums)
    #     res = 0
    #     left, right = 0, n-1
    #     while left < right:
    #         right = n - 1
    #         while left < right and nums[left] + nums[right] > target:
    #             right -= 1
    #         res += right - left
    #         left += 1
    #     return res % 1000000007

    # 超时了
    # def purchasePlans(self, nums: List[int], target: int) -> int:
    #     dic = defaultdict(int)
    #     dic[nums[0]] = 1
    #     res = 0
    #     for i in range(1, len(nums)):
    #         res += sum(dic[x] for x in dic if x <= target-nums[i])
    #         dic[nums[i]] += 1
    #     return res % 1000000007

    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        dic = defaultdict(int)
        dic[nums[0]] = 1
        res = 0
        for i in range(1, len(nums)):
            if nums[i] >= target:
                break
            res += sum(dic[x] for x in dic if x <= target-nums[i])
            dic[nums[i]] += 1
        return res % 1000000007


s = Solution()
nums = [2,5,3,5]
target = 6
print(s.purchasePlans(nums, target))

nums = [2,2,1,9]
target = 10
print(s.purchasePlans(nums, target))

nums = [2,2]
target = 10
print(s.purchasePlans(nums, target))

nums = [2,42]
target = 10
print(s.purchasePlans(nums, target))
