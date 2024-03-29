# 三数之和
from typing import List
from collections import Counter


class Solution:
    # # 我的方法
    # def isin(self, num, nums):
    #     for val in nums:
    #         if Counter(val) == Counter(num):
    #             return True
    #     return False
    #
    # def threeSum(self, nums):
    #     target = [-x for x in nums]
    #     hash_set = set()
    #     res = []
    #     for i in range(len(nums)-2):
    #         for j in range(i+1, len(nums)):
    #             if target[i]-nums[j] in hash_set:
    #                 tmp = [nums[i], target[i]-nums[j], nums[j]]
    #                 if not self.isin(tmp, res):
    #                     res.append([nums[i], target[i]-nums[j], nums[j]])
    #             hash_set.add(nums[j])
    #         hash_set.clear()
    #     return res

    # # 哈希表
    # def threeSum(self, nums):
    #     if len(nums) < 3:
    #         return []
    #     nums.sort()  # 方便判重
    #     res = set()  # 方便去重，不用 list 就是为了内循环中出现重复的无法去除，如 [0,0,0,0]。
    #     for idx, val in enumerate(nums[:-2]):
    #         # 去重，如果当前元素与前面的元素一样，就不用费尽心思，再进行比较一次了。时间提升了 1400ms。
    #         if idx > 0 and val == nums[idx-1]:  # 如果没有 idx > 0,则首次比较的时候是第一个与该数组的最后一个进行比较
    #             continue  # 第二个开始比较
    #
    #         hash_set = set()  # 写在里面，相当于在内循环结束后清空
    #         for j in range(idx+1, len(nums)):
    #             if nums[j] in hash_set:  # 找寻第三个数是否在集合中
    #                 res.add((val, -val-nums[j], nums[j]))
    #             hash_set.add(-val-nums[j])  # 第二个数也要添加在集合中
    #
    #     return list(map(list, res))

    # # 双指针
    # def threeSum(self, nums):
    #     if len(nums) < 3:
    #         return []
    #     nums.sort()  # 方便判重
    #     res = set()  # 方便去重
    #     for idx, val in enumerate(nums[:-2]):
    #         left, right = idx+1, len(nums)-1
    #         while left < right:
    #             s = nums[left] + nums[right] + val
    #             if s > 0:
    #                 right -= 1
    #             elif s < 0:
    #                 left += 1
    #             else:
    #                 res.add((val, nums[left], nums[right]))
    #                 left, right = left+1, right-1
    #     return list(map(list, res))

    # # 双指针, 判重，不用 set
    # def threeSum(self, nums):
    #     if len(nums) < 3:
    #         return []
    #     nums.sort()  # 方便判重
    #     res = []
    #     for idx, val in enumerate(nums[:-2]):
    #         if val > 0:
    #             return res
    #         if idx > 0 and val == nums[idx-1]:
    #             continue
    #         left, right = idx+1, len(nums)-1
    #         while left < right:
    #             s = nums[left] + nums[right] + val
    #             if s > 0:
    #                 # while left < right and nums[right] == nums[right-1]:  # 此处没有必要这样写，去重是针对值是确定的。
    #                 #     right -= 1
    #                 right -= 1
    #             elif s < 0:
    #                 left += 1
    #             else:
    #                 res.append([val, nums[left], nums[right]])
    #                 while left < right and nums[left] == nums[left+1]:  # 去重
    #                     left += 1
    #                 while left < right and nums[right] == nums[right-1]:
    #                     right -= 1
    #                 left, right = left+1, right-1
    #     return res

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     res = []
    #     for i, val in enumerate(nums[:-2]):
    #         if val > 0:
    #             return res
    #         left, right = i + 1, len(nums) - 1
    #         if val + nums[left] + nums[left+1] > 0:  # 最前面的三个数大于 0 则结束。
    #             return res
    #         if i > 0 and val == nums[i-1]:  # 连续的两个相同的跳过
    #             continue
    #
    #         while left < right:
    #             s = val + nums[left] + nums[right]
    #             if s > 0:
    #                 right -= 1
    #             elif s < 0:
    #                 left += 1
    #             else:
    #                 res.append([val, nums[left], nums[right]])
    #                 while left < right and nums[left] == nums[left+1]:
    #                     left += 1
    #                 while left < right and nums[right] == nums[right-1]:
    #                     right -= 1
    #                 left, right = left+1, right-1
    #     return res

    # 双指针
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     res = []
    #
    #     for i, num in enumerate(nums[:-2]):
    #         if num > 0:
    #             break
    #         if num + nums[i+1] + nums[i+2] > 0:
    #             break
    #         if num + nums[-1] + nums[-2] < 0:
    #             continue
    #
    #         if i > 0 and num == nums[i-1]:
    #             continue
    #
    #         left, right = i + 1, len(nums) - 1
    #         while left < right:
    #             tmp = num + nums[left] + nums[right]
    #             if tmp > 0:
    #                 right -= 1
    #             elif tmp < 0:
    #                 left += 1
    #             else:
    #                 res.append([num, nums[left], nums[right]])
    #                 while left < right and nums[right] == nums[right - 1]:
    #                     right -= 1
    #                 while left < right and nums[left] == nums[left+1]:
    #                     left += 1
    #                 left, right = left + 1, right - 1
    #     return res

    # # 哈希表
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     res = set()
    #     for i, num in enumerate(nums[:-2]):
    #         if i > 0 and num == nums[i-1]:
    #             continue
    #         record = set()
    #         for j in range(i+1, len(nums)):
    #             if -num-nums[j] in record:
    #                 res.add((num, -num-nums[j], nums[j]))
    #             record.add(nums[j])
    #     return list(map(list, res))

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     nums.sort()
    #     n = len(nums)
    #     for i, num in enumerate(nums[:-2]):
    #         if num > 0 or num+nums[i+1] > 0:
    #             break
    #         if i >= 1 and num == nums[i-1] or num + nums[-1] + nums[-2] < 0:
    #             continue
    #         j, k = i+1, n-1
    #         while j < k:
    #             val = num + nums[j] + nums[k]
    #             if val == 0:
    #                 res.append([num, nums[j], nums[k]])
    #                 while j < k and nums[j + 1] == nums[j]:
    #                     j += 1
    #                 j += 1
    #                 while j < k and nums[k-1] == nums[k]:
    #                     k -= 1
    #                 k -= 1
    #             elif val < 0:
    #                 while j < k and nums[j+1] == nums[j]:
    #                     j += 1
    #                 j += 1
    #             else:
    #                 while j < k and nums[k-1] == nums[k]:
    #                     k -= 1
    #                 k -= 1
    #     return res


    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     nums.sort()
    #     for i, num in enumerate(nums[:-2]):
    #         if num > 0 or num + nums[i+1] + nums[i+2] > 0:
    #             break
    #         if (i > 0 and num == nums[i-1]) or num + nums[-1] + nums[-2] < 0:
    #             continue
    #         left, right = i + 1, len(nums) - 1
    #         while left < right:
    #             val = num + nums[left] + nums[right]
    #             if val < 0:
    #                 left += 1
    #             elif val > 0:
    #                 right -= 1
    #             else:
    #                 res.append([num, nums[left], nums[right]])
    #                 while left < right and nums[left+1] == nums[left]:
    #                     left += 1
    #                 while left < right and nums[right-1] == nums[right]:
    #                     right -= 1
    #                 left, right = left + 1, right - 1
    #     return res

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     res = set()
    #     for i, num in enumerate(nums[:-2]):
    #         if i > 0 and num == nums[i-1]:
    #             continue
    #         record = set()
    #         for j in range(i+1, len(nums)):
    #             if -num-nums[j] in record:
    #                 res.add((num, nums[j], -num-nums[j]))
    #             record.add(nums[j])
    #     return list(map(list, res))

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     n = len(nums)
    #     res = []
    #     for i, num in enumerate(nums[:-2]):
    #         if num > 0:
    #             break
    #         if num + nums[i+1] + nums[i+2] > 0:
    #             break
    #         if i > 0 and num == nums[i-1]:
    #             continue
    #         if num + nums[-1] + nums[-2] < 0:
    #             continue
    #         left, right = i+1, n-1
    #         while left < right:
    #             val = num + nums[left] + nums[right]
    #             if val == 0:
    #                 res.append([num, nums[left], nums[right]])
    #                 while left < right and nums[left] == nums[left+1]:
    #                     left += 1
    #                 left += 1
    #                 while left < right and nums[right] == nums[right-1]:
    #                     right -= 1
    #                 right -= 1
    #             elif val > 0:
    #                 right -= 1
    #             else:
    #                 left += 1
    #     return res

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = set()
    #     nums.sort()
    #     for i, num in enumerate(nums[:-2]):
    #         if i > 0 and num == nums[i-1]:
    #             continue
    #         record = set()
    #         for j in range(i+1, len(nums)):
    #             if -num-nums[j] in record:
    #                 res.add((num, -num-nums[j], nums[j]))
    #             record.add(nums[j])
    #     return list(map(list, res))

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums[:-2]):
            if num + nums[i+1] + nums[i+2] > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            if num + nums[-1] + nums[-2] < 0:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                val = num + nums[left] + nums[right]
                if val == 0:
                    res.append([num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left, right = left + 1, right - 1
                elif val > 0:
                    right -= 1
                else:
                    left += 1
        return res


s = Solution()
nums = [0,0,0,0]
print(s.threeSum(nums))

nums = [0,0,0]
print(s.threeSum(nums))

nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))

nums = [-2,0,0,2,2]
print(s.threeSum(nums))

nums = [0,0]
print(s.threeSum(nums))

nums = [3,0,-2,-1,1,2]
print(s.threeSum(nums))

nums = []
print(s.threeSum(nums))