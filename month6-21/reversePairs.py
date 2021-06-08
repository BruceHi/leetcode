# 剑指 offer 51. 数组中的逆序对
from typing import List


class Solution:
    # def reversePairs(self, nums: List[int]) -> int:
    #     res = 0
    #     for i, num in enumerate(nums[:-1]):
    #         for j in range(i+1, len(nums)):
    #             if num > nums[j]:
    #                 res += 1
    #     return res

    # def reversePairs(self, nums: List[int]) -> int:
    #
    #     def merge_sort(left, right):  # left, right 表示索引号
    #         if left >= right:
    #             return 0
    #         mid = left + right >> 1
    #         res = merge_sort(left, mid) + merge_sort(mid+1, right)
    #         # 归并
    #         m, n = mid+1, right+1
    #         i, j = left, m
    #         tmp = []
    #         while i < m and j < n:
    #             if nums[i] > nums[j]:
    #                 tmp.append(nums[j])
    #                 res += m - i
    #                 j += 1
    #             else:
    #                 tmp.append(nums[i])
    #                 i += 1
    #         if i < m:
    #             tmp.extend(nums[i:m])
    #         else:
    #             tmp.extend(nums[j:n])
    #         # 不能写成 nums[i:n]，因为 i 肯定变了
    #         nums[left:n] = tmp
    #
    #         return res
    #
    #     return merge_sort(0, len(nums)-1)


    def reversePairs(self, nums: List[int]) -> int:

        def merge_sort(left, right):  # left, right 表示索引号
            if left >= right:
                return 0
            mid = left + right >> 1
            res = merge_sort(left, mid) + merge_sort(mid+1, right)
            # 归并
            m, n = mid+1, right+1
            i, j = left, m
            tmp = []
            while i < m and j < n:
                if nums[i] > nums[j]:
                    tmp.append(nums[j])
                    res += m - i
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            if i < m:
                tmp.extend(nums[i:m])
            else:
                tmp.extend(nums[j:n])
            nums[left:n] = tmp

            return res

        return merge_sort(0, len(nums)-1)


s = Solution()
nums = [7, 5, 6, 4]
print(s.reversePairs(nums))

nums = [1,3,2,3,1]
print(s.reversePairs(nums))
print(nums)

nums = [2, 3, 6, 7, 0, 1, 4, 5]
print(s.reversePairs(nums))
print(nums)
