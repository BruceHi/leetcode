from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=int, reverse=True)
        return nums[k-1]


s = Solution()
nums = ["3","6","7","10"]
k = 4
print(s.kthLargestNumber(nums, k))

nums = ["2","21","12","1"]
k = 3
print(s.kthLargestNumber(nums, k))

nums = ["0","0"]
k = 2
print(s.kthLargestNumber(nums, k))
