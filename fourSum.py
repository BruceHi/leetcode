# 四数之和
class Solution:
    def fourSum(self, nums, target: int):
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i, v in enumerate(nums[:-3]):
            if v+nums[i+1]+nums[i+2]+nums[i+3] > target:
                return res
            if v+nums[-1]+nums[-2]+nums[-3] < target:
                continue
            if i > 0 and v == nums[i-1]:  # 第1次去重
                continue

            for j in range(i+1, len(nums)-2):
                if v+nums[j]+nums[j+1]+nums[j+2] > target:
                    break
                if v+nums[j]+nums[-1]+nums[-2] < target:
                    continue
                if j-i > 1 and nums[j] == nums[j-1]:  # 第二次去重
                    continue
                left, right = j+1, len(nums)-1

                while left < right:
                    s = v + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        res.append([v, nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left, right = left+1, right-1

        return res


s = Solution()
nums = [0,0,0,0]
target = 0
print(s.fourSum(nums, target))


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(s.fourSum(nums, target))