# 345.反转字符串中的元音字母


class Solution:
    def reverseVowels(self, s: str) -> str:
        nums = [c for c in s]
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in 'aeiouAEIOU':
                i += 1
            while i < j and s[j] not in 'aeiouAEIOU':
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j-1
        return ''.join(nums)


obj = Solution()
s = "hello"
print(obj.reverseVowels(s))

s = "leetcode"
print(obj.reverseVowels(s))

s = "aA"
print(obj.reverseVowels(s))

s = ".,"
print(obj.reverseVowels(s))