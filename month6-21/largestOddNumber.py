class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) & 1:
                return num[:i+1]
        return ''


s = Solution()
num = "52"
print(s.largestOddNumber(num))

num = "4206"
print(s.largestOddNumber(num))

num = "35427"
print(s.largestOddNumber(num))
