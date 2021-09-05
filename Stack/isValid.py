# def isValid(self, s: str) -> bool:
#     stack = []
#     for i in s:
#         if i in {'(', '[', '{'}:
#             stack.append(i)
#         elif not len(stack):
#             return False
#         elif ord(stack[-1]) + 1 == ord(i) or ord(stack[-1]) + 2 == ord(i):
#             stack.pop()
#         else:
#             return False
#     return len(stack) == 0


# 有效的括号
class Solution:
    # def isValid(self, s: str) -> bool:
    #     stack = []
    #     paren_map = {')': '(', ']': '[', '}': '{'}
    #     for i in s:
    #         if i not in paren_map:
    #             stack.append(i)
    #         elif not stack or paren_map[i] != stack.pop():
    #             return False
    #         # elif not stack or stack[-1] != hashmap[i]:
    #         #     return False
    #         # else:
    #         #     stack.pop()
    #     return not stack

    def isValid(self, s: str) -> bool:
        if len(s) & 1:
            return False
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c not in dic:
                stack.append(c)
            elif not stack or dic[c] != stack.pop():
                return False
        return not stack


s = Solution()
string = "()"
print(s.isValid(string))

string = "()[]{}"
print(s.isValid(string))

string = "(]"
print(s.isValid(string))

string = "([)]"
print(s.isValid(string))

string = "{[]}"
print(s.isValid(string))

string = ''
print(s.isValid(string))

string = '['
print(s.isValid(string))

string = ']'
print(s.isValid(string))
