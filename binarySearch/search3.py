class Solution:
    # 第一个大于或等于目标的索引值，收缩左边界
    def first_large_or_equal(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right >> 1  # 地板除，取下届
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[right] >= target:
            return right
        return -1

    # 最后一个小于或等于目标的索引值，收缩右边
    def last_less_or_equal(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right + 1 >> 1  # 取上界
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[right] <= target:
            return right
        return -1




s = Solution()
print('查找第一个大于等于给定值的元素')

###
nums = [0, 1, 1, 1, 2, 7]
target = 3
print(s.first_large_or_equal(nums, target))

nums = [0, 1, 1, 1, 6, 6,  9]
target = 5
print(s.first_large_or_equal(nums, target))

nums = []
target = 5
print(s.first_large_or_equal(nums, target))

nums = [5]
target = 8
print(s.first_large_or_equal(nums, target))

nums = [4, 4, 4, 4, 7, 8, 8]
target = 10
print(s.first_large_or_equal(nums, target))

nums = [3, 4, 4, 4, 7, 8]
target = 4
print(s.first_large_or_equal(nums, target))


print('查找最后一个小于等于给定值的元素')

###
nums = [0, 1, 1, 1, 2, 7]
target = 3
print(s.last_less_or_equal(nums, target))

nums = [0, 1, 1, 1, 6, 6,  9]
target = 5
print(s.last_less_or_equal(nums, target))

nums = []
target = 5
print(s.last_less_or_equal(nums, target))

nums = [5]
target = 4
print(s.last_less_or_equal(nums, target))

nums = [4, 4, 4, 4, 7, 8, 8]
target = 8
print(s.last_less_or_equal(nums, target))

nums = [3, 4, 4, 4, 7, 8]
target = 4
print(s.last_less_or_equal(nums, target))
