from typing import List


class Solution:
    # 超时 50 / 57 个通过测试用例
    # def sumOfBeauties(self, nums: List[int]) -> int:
    #     res = 0
    #     for i in range(1, len(nums)-1):
    #         if all([x < nums[i] for x in nums[:i]]) and all([nums[i] < x for x in nums[i+1:]]):
    #             res += 2
    #         elif nums[i-1] < nums[i] < nums[i+1]:
    #             res += 1
    #     return res

    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0] * n
        res[0] = 2
        for i in range(1, n-1):
            if nums[i - 1] < nums[i] < nums[i + 1]:
                res[i] += 1
            if res[i] == 1 and res[i-1] == 2:
                if all([nums[i] < x for x in nums[i+2:]]):
                    res[i] += 1
        return sum(res)


s = Solution()
nums = [1,2,3]
print(s.sumOfBeauties(nums))

nums = [2,4,6,4]
print(s.sumOfBeauties(nums))

nums = [3,2,1]
print(s.sumOfBeauties(nums))

