from typing import List



class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        m = (n + 1) // 2  # 注意这个 要多一个 [1, 2, 3], [1, 2, 3, 4]
        res = []
        for i in range(m):
            res.append(nums[i])
            if i + m < n:
                res.append(nums[i+m])
        return res




s = Solution()
nums = [1,2,3,4,5]
print(s.rearrangeArray(nums))

nums = [6,2,0,9,7]
print(s.rearrangeArray(nums))

nums = [1,2,3]
print(s.rearrangeArray(nums))

nums = [1,2,3, 5, 9]
print(s.rearrangeArray(nums))

nums = [1,5,2,6,3,7,4,8]
print(s.rearrangeArray(nums))

nums = [0,4,1,5,3]
print(s.rearrangeArray(nums))

nums = [0,5,2,1,4]
print(s.rearrangeArray(nums))