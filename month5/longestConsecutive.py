# 最长连续序列
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


class Solution:

    # 哈希表
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)

        for num in nums:
            if num-1 not in nums_set:
                cur_num = num
                length = 1

                while cur_num+1 in nums_set:
                    cur_num += 1
                    length += 1

                res = max(res, length)

        return res


s = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(s.longestConsecutive(nums))
