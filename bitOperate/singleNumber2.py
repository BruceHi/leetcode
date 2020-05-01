# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
from collections import Counter
class Solution:
    # 词频
    def singleNumber(self, nums):
        count = Counter(nums)
        # res = []
        # for key in count:
        #     if count[key] == 1:
        #         res.append(key)  # res += [key]
        #         if len(res) == 2:
        #             break
        # return res
        return [x for x in count if count[x] == 1]


s = Solution()
a = [1,2,1,3,2,5]
print(s.singleNumber(a))
