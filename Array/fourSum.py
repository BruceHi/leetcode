# 18.四数之和
from typing import List


class Solution:
    # def fourSum(self, nums, target: int):
    #     if len(nums) < 4:
    #         return []
    #     nums.sort()
    #     res = []
    #     for i, v in enumerate(nums[:-3]):
    #         if v+nums[i+1]+nums[i+2]+nums[i+3] > target:
    #             return res
    #         if v+nums[-1]+nums[-2]+nums[-3] < target:
    #             continue
    #         if i > 0 and v == nums[i-1]:  # 第1次去重
    #             continue
    #
    #         for j in range(i+1, len(nums)-2):
    #             if v+nums[j]+nums[j+1]+nums[j+2] > target:
    #                 break
    #             if v+nums[j]+nums[-1]+nums[-2] < target:
    #                 continue
    #             if j-i > 1 and nums[j] == nums[j-1]:  # 第二次去重
    #                 continue
    #             left, right = j+1, len(nums)-1
    #
    #             while left < right:
    #                 s = v + nums[j] + nums[left] + nums[right]
    #                 if s < target:
    #                     left += 1
    #                 elif s > target:
    #                     right -= 1
    #                 else:
    #                     res.append([v, nums[j], nums[left], nums[right]])
    #                     while left < right and nums[left] == nums[left+1]:
    #                         left += 1
    #                     while left < right and nums[right] == nums[right-1]:
    #                         right -= 1
    #                     left, right = left+1, right-1
    #
    #     return res

    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     nums.sort()
    #     res = []
    #     n = len(nums)
    #
    #     for i, num in enumerate(nums[:-3]):
    #         if i > 0 and num == nums[i-1]:
    #             continue
    #
    #         for j in range(i+1, n-2):
    #             if j > i+1 and nums[j] == nums[j-1]:
    #                 continue
    #
    #             left, right = j+1, n - 1
    #             while left < right:
    #                 tmp = num + nums[j] + nums[left] + nums[right]
    #                 if tmp < target:
    #                     left += 1
    #                 elif tmp > target:
    #                     right -= 1
    #                 else:
    #                     res.append([num, nums[j], nums[left], nums[right]])
    #                     while left < right and nums[left] == nums[left+1]:
    #                         left += 1
    #                     while left < right and nums[right] == nums[right-1]:
    #                         right -= 1
    #                     left, right = left + 1, right - 1
    #     return res

    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     nums.sort()
    #     res = []
    #     n = len(nums)
    #
    #     for i, num in enumerate(nums[:-3]):
    #         if num + nums[i+1] + nums[i+2] + nums[i+3] > target:
    #             break
    #         if num + nums[-1] + nums[-2] + nums[-3] < target:
    #             continue
    #         if i > 0 and num == nums[i-1]:
    #             continue
    #
    #         for j in range(i+1, n-2):
    #             if num + nums[j] + nums[j+1] + nums[j+2] > target:
    #                 break
    #             if num + nums[j] + nums[-1] + nums[-2] < target:
    #                 continue
    #             if j > i+1 and nums[j] == nums[j-1]:
    #                 continue
    #
    #             left, right = j+1, n - 1
    #             while left < right:
    #                 tmp = num + nums[j] + nums[left] + nums[right]
    #                 if tmp < target:
    #                     left += 1
    #                 elif tmp > target:
    #                     right -= 1
    #                 else:
    #                     res.append([num, nums[j], nums[left], nums[right]])
    #                     while left < right and nums[left] == nums[left+1]:
    #                         left += 1
    #                     while left < right and nums[right] == nums[right-1]:
    #                         right -= 1
    #                     left, right = left + 1, right - 1
    #     return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i, num in enumerate(nums[:-3]):
            if num + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if i > 0 and num == nums[i-1]:
                continue
            if num + nums[-1] + nums[-2] + nums[-3] < target:
                continue

            for j in range(i+1, n-2):
                if num + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if num + nums[j] + nums[-1] + nums[-2] < target:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    val = num + nums[j] + nums[left] + nums[right]
                    if val < target:
                        left += 1
                    elif val > target:
                        right -= 1
                    else:
                        res.append([num, nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left, right = left+1, right-1
        return res

s = Solution()
nums = [0,0,0,0]
target = 0
print(s.fourSum(nums, target))


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(s.fourSum(nums, target))

nums = [-1,0,1,2,-1,-4]
target = -1
print(s.fourSum(nums, target))

nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
print(s.fourSum(nums, target))

nums = [2,2,2,2,2]
target = 8
print(s.fourSum(nums, target))
