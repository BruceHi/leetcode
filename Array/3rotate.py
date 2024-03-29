# def rotate(nums, k):
#     temp = []
#     if len(nums) > k:
#         for i in range(-k, 0):
#             temp.append(nums[i])
#
#         j = len(nums)
#         while j >= k:
#             nums[j - 1] = nums[j - 1 - k]
#             j -= 1
#
#         for i in range(0, k):
#             nums[i] = temp[i]
#
#     for i in range(k % len(nums)):
#         nums.insert(0, nums.pop())


# def reverse(nums):
#     for i in range(int(len(nums) / 2)):  # 循环不能全写完，否则又翻过来了
#         nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i],  nums[i]
#
#
# def rotate(nums, k):
#     reverse(nums)
#     reverse(nums[: k % len(nums)])  # 切片会生成一个新的引用对象的。对这个对象操作，对原来对象没影响。
#     reverse(nums[k % len(nums):])


# def rotate(nums, k):
#     n = len(nums)
#     k %= n
#     nums[:] = nums[::-1]
#     # nums[:] = nums[k - 1::-1] + nums[: k - 1: -1]  # 前k个元素反转+剩余的元素反转。
#     nums[:] = nums[:k][::-1] + nums[k:][::-1]

# 推荐写法
# def rotate(nums, k):
#     k %= len(nums)
#     nums = nums[::-1]
#     nums = nums[:k][::-1] + nums[k:][::-1]

from typing import List


# def rotate(nums: List[int], k: int) -> None:
#     k %= len(nums)
#     nums[:] = nums[-k:] + nums[:-k]
#     reversed(nums)


# 真·原地算法
# def rotate(nums: List[int], k: int) -> None:
#
#     def swap(nums, left, right):
#         while left < right:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#             right -= 1
#
#     nums.reverse()
#     k %= len(nums)
#     swap(nums, 0, k-1)
#     swap(nums, k, len(nums)-1)

# def rotate(nums: List[int], k: int) -> None:
#     n = len(nums)
#     k %= n
#     if not k:
#         return
#     nums[:n-k] = reversed(nums[:n-k])
#     nums[-k:] = reversed(nums[-k:])
#     nums[:] = reversed(nums)

# def rotate(nums: List[int], k: int) -> None:
#     n = len(nums)
#     new = [0] * n
#     for i, num in enumerate(nums):
#         new[(i+k) % n] = num
#     nums[:] = new

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:] = nums[:k][::-1] + nums[k:][::-1]


s = Solution()
list1 = [1,2,3,4,5,6,7]
s.rotate(list1, 3)
print(list1)

list1 = [-1,-100,3,99]
s.rotate(list1, 2)
print(list1)

list1 = [-1]
s.rotate(list1, 2)
print(list1)

list1 = [1, 2]
s.rotate(list1, 3)
print(list1)

list1 = [1, 2, 3]
s.rotate(list1, 4)
print(list1)

list1 = [1, 2]
s.rotate(list1, 0)
print(list1)