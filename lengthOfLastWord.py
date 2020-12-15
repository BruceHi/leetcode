# 58. 最后一个单词的长度
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s.split():  # 若是分割结束之后是空的，即结果为 []，则直接返回 0.
            return 0
        return len(s.split()[-1])
    #
    # def lengthOfLastWord(self, s: str) -> int:
    #     # print(s.strip())
    #     # print(s.strip().split())
    #     # print(s.strip().split(''))  # 若是空结果，则返回 ['']。必须前去掉前后面空格。再split(' ')才不会出错
    #     return len(s.strip().split(' ')[-1])



obj = Solution()
s = "Hello World"
print(obj.lengthOfLastWord(s))

s = ""
print(obj.lengthOfLastWord(s))

s = " "
print(obj.lengthOfLastWord(s))
