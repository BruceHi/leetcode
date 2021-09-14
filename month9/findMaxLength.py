# 525. 连续数组
# 找到含有相同数量的 0 和 1 的**最长**连续子数组，并返回该子数组的长度。
from typing import List


class Solution:
    # 前缀和, 其中 count 就是前缀和, 将 0 替换为 -1
    # 相当于求：最长的连续子数组，其元素和等于 0
    # def findMaxLength(self, nums: List[int]) -> int:
    #     res = 0
    #     count = 0
    #     dic = {0: -1}
    #     for i, num in enumerate(nums):
    #         if num == 1:
    #             count += 1
    #         else:
    #             count -= 1
    #         if count in dic:
    #             res = max(res, i-dic[count])
    #         else:
    #             dic[count] = i
    #     return res

    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: -1}
        res = 0
        prefix = 0
        for i, num in enumerate(nums):
            if num == 1:
                prefix += 1
            else:
                prefix -= 1
            if prefix in dic:
                res = max(res, i-dic[prefix])
            else:
                dic[prefix] = i
        return res


s = Solution()
nums = [0,1]
print(s.findMaxLength(nums))

nums = [0,1,0]
print(s.findMaxLength(nums))
