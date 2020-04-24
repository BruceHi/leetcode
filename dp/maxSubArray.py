# 连续子数组的最大和
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        dp, max_val = float('-inf'), float('-inf')
        for num in nums:
            dp = max(num, dp+num)
            max_val = max(max_val, dp)

        return max_val


s = Solution()
a = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(a))

a = []
print(s.maxSubArray(a))
