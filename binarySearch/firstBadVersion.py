# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

# 第一个错误的版本
# 返回第一个结果为 True 的值。

def isBadVersion(version):
    pass


class Solution:
    # def firstBadVersion(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     left, right = 1, n
    #     while left < right:
    #         mid = left + right >> 1
    #         if isBadVersion(mid):
    #             right = mid
    #         else:
    #             left = mid + 1
    #     return right

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = left + right >> 1
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left

