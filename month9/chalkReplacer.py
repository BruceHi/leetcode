# 1894. 找到需要补充粉笔的学生编号
from typing import List


class Solution:
    # 超时
    # def chalkReplacer(self, chalk: List[int], k: int) -> int:
    #     n = len(chalk)
    #     i = 0
    #     while k >= 0:
    #         k -= chalk[i]
    #         i = (i + 1) % n
    #     return (i-1) % n


    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total
        for i, c in enumerate(chalk):
            if c > k:
                return i
            k -= c


s = Solution()
chalk = [5,1,5]
k = 22
print(s.chalkReplacer(chalk, k))

chalk = [3,4,1,2]
k = 25
print(s.chalkReplacer(chalk, k))
