# import bisect
#
#
# def function(nums):
#     max_val = max(nums)
#     idx = nums.index(max_val)
#     res = nums[:idx]
#     for num in nums[idx:]:
#         if num not in res:
#             i = bisect.insort_left(nums, num)
#             nums.insert()
#     return res
#
#
# nums = [1, 2, 2, 5, 10, 9, 8, 2, 1, 1]
# print(function(nums))

import re


def function(s):
    p = r'(https|https)'