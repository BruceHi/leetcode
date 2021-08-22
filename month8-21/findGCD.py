from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)
        return gcd(min(nums), max(nums))


s = Solution()
nums = [2,5,6,9,10]
print(s.findGCD(nums))

nums = [7,5,6,8,3]
print(s.findGCD(nums))

nums = [3,3]
print(s.findGCD(nums))
