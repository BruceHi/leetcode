# 594. 最长和谐子序列
from typing import List
from collections import Counter


class Solution:
    # def findLHS(self, nums: List[int]) -> int:
    #     dic = defaultdict(list)
    #     for num in nums:
    #         dic[str(num)+'+'].append(num)
    #         dic[str(num)+'-'].append(num)
    #         dic[str(num-1)+'+'].append(num)
    #         dic[str(num+1)+'-'].append(num)
    #     res = 0
    #     for v in dic.values():
    #         if max(v) - min(v) == 1:
    #             res = max(res, len(v))
    #     return res

    # def findLHS(self, nums: List[int]) -> int:
    #     res = 0
    #     count = Counter(nums)
    #     for k, v in count.items():
    #         if count[k+1] > 0:
    #             res = max(res, v+count[k+1])
    #     return res

    # def findLHS(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     res = 0
    #     sort_nums = sorted(set(nums))
    #     for num in sort_nums:
    #         if num+1 in count:
    #             res = max(res, count[num]+count[num+1])
    #     return res

    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for k in count:
            if k+1 in count:
                res = max(res, count[k]+count[k+1])
        return res


s = Solution()
nums = [1,3,2,2,5,2,3,7]
print(s.findLHS(nums))

nums = [1,2,3,4]
print(s.findLHS(nums))

nums = [1,1,1,1]
print(s.findLHS(nums))
