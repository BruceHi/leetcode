# 655. 非递减数列
from typing import List


class Solution:

    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if changed:
                    return False
                changed = True

                # 修改后者
                if i > 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
        return True


s = Solution()
nums = [4,2,3]
print(s.checkPossibility(nums))

nums = [4,2,1]
print(s.checkPossibility(nums))

nums = [-1,4,2,3]
print(s.checkPossibility(nums))

nums = [-1,1,2,3]
print(s.checkPossibility(nums))

nums = [3,4,2,3]
print(s.checkPossibility(nums))

nums = [3,4,2,5]
print(s.checkPossibility(nums))
