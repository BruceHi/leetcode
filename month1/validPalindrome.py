# 680. 验证回文子串 2
class Solution:
    # 超时
    # def validPalindrome(self, s: str) -> bool:
    #     def isvalid(s):
    #         return s == s[::-1]
    #
    #     if isvalid(s):
    #         return True
    #     for i in range(len(s)):
    #         if isvalid(s[:i] + s[i+1:]):
    #             return True
    #
    #     return False

    # def validPalindrome(self, s: str) -> bool:
    #     def isvalid(s):
    #         return s == s[::-1]
    #
    #     low, high = 0, len(s) - 1
    #     while low < high:
    #         if s[low] == s[high]:
    #             low, high = low+1, high-1
    #         else:
    #             return isvalid(s[low+1:high+1]) or isvalid(s[low:high])
    #
    #     return True

    def validPalindrome(self, s: str) -> bool:

        def is_valid(s):
            return s == s[::-1]

        n = len(s)
        left, right = 0, n-1
        while left < right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
            else:
                return is_valid(s[left:right]) or is_valid(s[left+1:right+1])
        return True


obj = Solution()
s = "aba"
print(obj.validPalindrome(s))

s = "abca"
print(obj.validPalindrome(s))

s = "abc"
print(obj.validPalindrome(s))
