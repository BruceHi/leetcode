# 众数
# 169. 多数元素
# 剑指 Offer 39. 数组中出现次数超过一半的数字
from typing import List
from collections import Counter


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     counts = Counter(nums)
    #     return max(counts.keys(), key=counts.get)  # 很是厉害,值得注意

    # def majorityElement(self, nums: List[int]) -> int:
    #     hash_map = {}
    #     for num in nums:
    #         hash_map[num] = hash_map.get(num, 0) + 1
    #         if hash_map[num] > len(nums) >> 1:
    #             return num

    # def majorityElement(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     res = count.most_common(1)
    #     return res[0][0]

    # def majorityElement(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     res, = [key for key in count if count[key] > len(nums) // 2]
    #     return res

    # def majorityElement(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     return max(count, key=count.get)

    # 剑指 offer 要求返回-1
    # def majorityElement(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     res = [key for key in count if count[key] > len(nums) // 2]
    #     return res[0] if res else -1

    # def majorityElement(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     for k, v in count.items():
    #         if v > len(nums) // 2:
    #             return k
    #     return -1

    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 1, nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
        return candidate



s = Solution()
nums = [3,2,3]
print(s.majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(s.majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(s.majorityElement(nums))

# 错误示例，不符号多数元素
# nums = [3, 2]
# print(s.majorityElement(nums))
