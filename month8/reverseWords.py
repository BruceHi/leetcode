# 翻转字符串中的单词 3
class Solution:
    # def reverseWords(self, s: str) -> str:
    #     res = ''
    #     i = 0
    #     for j, c in enumerate(s):
    #         if c == ' ':
    #             res += s[i:j][::-1] + ' '
    #             i = j + 1
    #     return res + s[i:][::-1]

    def reverseWords(self, s: str) -> str:
        return ' '.join(a[::-1] for a in s.split())



obj = Solution()
print(obj.reverseWords("Let's take LeetCode contest"))

print(obj.reverseWords("Let's take LeetCode"))