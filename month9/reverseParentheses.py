# 1190. 反转每队括号间的字串
class Solution:
    # def reverseParentheses(self, s: str) -> str:
    #     stack = []
    #     pre = ''
    #     for c in s:
    #         if c == ')':
    #             while stack and stack[-1] != '(':
    #                 pre = stack.pop() + pre
    #             stack.pop()
    #             stack.append(pre[::-1])
    #             pre = ''
    #         elif c == '(':
    #             stack.append(pre)
    #             pre = ''
    #             stack.append(c)
    #         else:
    #             pre += c
    #     return ''.join(stack) + pre

    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = ''
        for c in s:
            if c == '(':
                stack.append(res)
                res = ''
            elif c == ')':
                res = stack.pop() + res[::-1]  # 相当于去除左括号
            else:
                res += c
        return res



obj = Solution()
s = "(abcd)"
print(obj.reverseParentheses(s))

s = "(u(love)i)"
print(obj.reverseParentheses(s))

s = "(ed(et(oc))el)"
print(obj.reverseParentheses(s))

s = "a(bcdefghijkl(mno)p)q"
print(obj.reverseParentheses(s))
