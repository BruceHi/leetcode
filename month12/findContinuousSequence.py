# 剑指 offer 57-2.和为 s 的连续正整数序列
# 滑动窗口
from typing import List

class Solution:
    # def findContinuousSequence(self, target: int) -> List[List[int]]:
    #     if target <= 2:
    #         return []
    #     res = []
    #     mid = target // 2
    #     if mid + mid + 1 == target:
    #         res.append([mid, mid+1])
    #     while True:

    # 滑动窗口
    # https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/
    # def findContinuousSequence(self, target: int) -> List[List[int]]:
    #     i = 1
    #     j = 1
    #     count = 0
    #     res = []
    #
    #     while i <= target // 2:
    #         if count < target:  # 右边界向右移动
    #             count += j
    #             j += 1
    #         elif count > target:  # 左边界向右移动
    #             count -= i
    #             i += 1
    #         else:
    #             res.append(list(range(i, j)))
    #             count -= i  # 左边界向右移动
    #             i += 1
    #     return res

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j = 1, 1
        res = []
        count = 0
        while i <= target // 2:
            if count < target:
                count += j
                j += 1
            elif count > target:
                count -= i
                i += 1
            else:
                res.append(list(range(i, j)))
                count -= i
                i += 1
        return res


s = Solution()
target = 9
print(s.findContinuousSequence(target))

target = 15
print(s.findContinuousSequence(target))
