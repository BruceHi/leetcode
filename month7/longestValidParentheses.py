# 有效括号的字串长度，并非看括号的个数
class Solution:

    # def longestValidParentheses(self, s: str) -> int:
    #     stack, res = [-1], 0
    #     for i, c in enumerate(s):
    #         if c == '(':
    #             stack.append(i)
    #         else:
    #             stack.pop()  # 先弹出一个进行匹配，这点还是有点反常识的。
    #             if stack:
    #                 res = max(res, i-stack[-1])
    #             else:
    #                 stack.append(i)
    #     return res

    # def longestValidParentheses(self, s: str) -> int:
    #     res = 0
    #     stack = [-1]
    #     for i, c in enumerate(s):
    #         if c == '(':
    #             stack.append(i)
    #         else:
    #             if len(stack) == 1:
    #                 stack.append(i)
    #             elif s[stack[-1]] == ')':
    #                 stack.append(i)
    #             else:
    #                 stack.pop()
    #                 res = max(res, i-stack[-1])
    #     return res

    def longestValidParentheses(self, s: str) -> int:
        res, stack = 0, [-1]  # 注意 stack 初始化
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)  # 栈里面放的全都是 '(' 的索引，只有一种例外，那就是首位不得不放 ‘）’ 的索引。
            else:
                stack.pop()
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
