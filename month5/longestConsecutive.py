# 最长连续序列
# 不要求顺序
from typing import List

# 使用并查集，失败
# class UnionFind:
#     def __init__(self, nums):
#         n = len(nums)
#         self.parent = [_ for _ in range(n)]
#         self.count = n
#         self.rank = [1] * n
#
#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]
#
#     def union(self, x, y):
#         rootx = self.find(x)
#         rooty = self.find(y)
#         if self.rank[rootx] < self.rank[rooty]:
#             self.parent[rootx] = self.parent[rooty]
#         else:
#             if self.rank[rootx] == self.rank[rooty]:
#                 self.rank[rootx] += 1
#             self.parent[rooty] = self.parent[rootx]
#         self.count -= 1
#
#
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         n = len(nums)
#         if not n:
#             return 0
#         hash_set = set(nums)
#
#         left, right = 0, n-1
#         uf = UnionFind(nums)
#
#         for i in range(1, n):
#             if nums[i] in
#
#         return uf.count


# class Solution:
#
#     # 哈希表
#     def longestConsecutive(self, nums: List[int]) -> int:
#         res = 0
#         nums_set = set(nums)
#
#         for num in nums:
#             if num-1 not in nums_set:
#                 cur_num = num
#                 length = 1
#
#                 while cur_num+1 in nums_set:
#                     cur_num += 1
#                     length += 1
#
#                 res = max(res, length)
#
#         return res

class Solution:

    # 排序，时间复杂度为 O（n log n）
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     nums.sort()
    #
    #     res, count = 1, 1
    #     for i in range(1, len(nums)):
    #         if nums[i] != nums[i-1]:  # 去重
    #             if nums[i] == nums[i-1] + 1:
    #                 count += 1
    #             else:
    #                 count = 1
    #             res = max(res, count)
    #     return res

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     nums = set(nums)
    #
    #     res = 0
    #     for num in nums:
    #         if num - 1 not in nums:
    #             length = 1
    #             tmp = num + 1
    #             while tmp in nums:
    #                 length += 1
    #                 tmp += 1
    #             res = max(res, length)
    #
    #     return res

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     nums = list(set(nums))
    #     nums.sort()
    #     res = 0
    #     i = 0
    #     for j, num in enumerate(nums[:-1]):  # 使用 j-i 的方法统计，不太好
    #         if num + 1 != nums[j+1]:
    #             res = max(res, j-i+1)
    #             i = j+1
    #     res = max(res, len(nums) - i)
    #     return res

    # 使用 哈希表
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     nums = set(nums)
    #     res = 0
    #     for num in nums:
    #         if num - 1 not in nums:
    #             count = 1
    #             while num + 1 in nums:
    #                 count += 1
    #                 num = num + 1
    #             res = max(res, count)
    #     return res

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                count = 1
                while num + 1 in nums:
                    count += 1
                    num += 1
                res = max(res, count)
        return res


s = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(s.longestConsecutive(nums))

nums = []
print(s.longestConsecutive(nums))

nums = [0, -1]
print(s.longestConsecutive(nums))

nums = [1,2,0,1]  # 还需要去重
print(s.longestConsecutive(nums))

nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(s.longestConsecutive(nums))
