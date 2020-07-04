# 有效括号的字串长度，并非看括号的个数
class Solution:
    # def longestValidParentheses(self, s: str) -> int:
    #     stack, res = [], 0
    #     for c in s:
    #         if c == '(':
    #             stack.append(c)
    #         else:
    #             if stack and stack[-1] == '(':
    #                 stack.pop()
    #                 res += 2
    #             else:
    #                 stack.append(c)
    #     return res

    def longestValidParentheses(self, s: str) -> int:
        stack, res = [-1], 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()  # 先弹出一个进行匹配，这点还是有点反常识的。
                if stack:
                    res = max(res, i-stack[-1])
                else:
                    stack.append(i)
        return res


obj = Solution()
s = "(()"
print(obj.longestValidParentheses(s))

s = ")()())"
print(obj.longestValidParentheses(s))

s = ")"
print(obj.longestValidParentheses(s))

s = ""
print(obj.longestValidParentheses(s))

s = "()(()"
print(obj.longestValidParentheses(s))
