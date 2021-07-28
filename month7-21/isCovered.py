# 1893. 检查是否区域内所有整数都被覆盖
from typing import List


class Solution:
    # 每次求交集
    # def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
    #     nums = []
    #     for a, b in ranges:
    #         if not (b < left or a > right):
    #             nums.extend(range(max(a, left), min(b, right)+1))
    #             if set(nums) == set(range(left, right+1)):
    #                 return True
    #     return False

    # 合并区间
    # def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
    #     ranges.sort()
    #     nums = [ranges[0]]
    #     for a, b in ranges[1:]:
    #         if a > nums[-1][1] + 1:
    #             nums.append([a, b])
    #         else:
    #             nums[-1][1] = max(nums[-1][1], b)
    #
    #     for a, b in nums:
    #         if a <= left and b >= right:
    #             return True
    #     return False

    # 利用提示所给的区间信息
    # def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
    #     nums = [0] * 51
    #     for a, b in ranges:
    #         for i in range(a, b+1):
    #             nums[i] += 1
    #     return 0 not in nums[left:right+1]

    # 差分数组
    # 首尾加一，末尾的下一位加一，保证在区间内的前缀和大于或等于 1
    # https://leetcode-cn.com/problems/
    # check-if-all-the-integers-in-a-range-are-covered/solution/yi-ti-san-jie-bao-li-you-hua-chai-fen-by-w7xv/
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52
        for a, b in ranges:
            diff[a] += 1
            diff[b+1] -= 1

        pre_sum = [0] * 52
        for i in range(1, 51):
            pre_sum[i] = pre_sum[i-1] + diff[i]

        for i in range(left, right+1):
            if pre_sum[i] < 1:
                return False
        return True

s = Solution()
ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5
print(s.isCovered(ranges, left, right))

ranges = [[1,10],[10,20]]
left = 21
right = 21
print(s.isCovered(ranges, left, right))

ranges = [[22,48],[46,47]]
left = 28
right = 33
print(s.isCovered(ranges, left, right))
