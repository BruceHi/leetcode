# 1047. 删除
class Solution:
    # def removeDuplicates(self, S: str) -> str:
    #     stack = []
    #     for c in S:
    #         if not stack or stack[-1] != c:
    #             stack.append(c)
    #         else:
    #             while stack and stack[-1] == c:
    #                 stack.pop()
    #     return ''.join(stack)

    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


obj = Solution()
S = "abbaca"
print(obj.removeDuplicates(S))

S = ""
print(obj.removeDuplicates(S))
