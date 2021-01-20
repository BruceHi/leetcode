# 844. 比较含退格的字符串
# 匹配问题都是栈的强项
class Solution:
    # 使用双指针，失败
    # def backspaceCompare(self, S: str, T: str) -> bool:
    #     m, n = len(S), len(T)
    #     i, j = m-1, n-1
    #     while i >= 0 and j >= 0:
    #         while i >= 0 and S[i] == '#':
    #             i -= 1
    #         while j >= 0 and T[j] == '#':
    #             i -= 1
    #

    # def backspaceCompare(self, S: str, T: str) -> bool:
    #     def backspace(attrs):
    #         res = ''
    #         i = len(attrs) - 1
    #         while i >= 0:
    #             if attrs[i] == '#':
    #                 i -= 2
    #             res = attrs[i] + res
    #             i -= 1
    #         return res
    #
    #     print(backspace(S))
    #     print(backspace(T))
    #     return backspace(S) == backspace(T)

    # 栈
    # def backspaceCompare(self, S: str, T: str) -> bool:
    #     def backspace(attrs):
    #         stack = []
    #         for c in attrs:
    #             if c == '#':
    #                 if stack:
    #                     stack.pop()
    #             else:
    #                 stack.append(c)
    #         return ''.join(stack)
    #     return backspace(S) == backspace(T)

    def backspaceCompare(self, S: str, T: str) -> bool:
        def backspace(attrs):
            stack = []
            for c in attrs:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        return backspace(S) == backspace(T)


obj = Solution()
S = "ab#c"
T = "ad#c"
print(obj.backspaceCompare(S, T))

S = "ab##"
T = "c#d#"
print(obj.backspaceCompare(S, T))

S = "a##c"
T = "#a#c"
print(obj.backspaceCompare(S, T))

S = "a#c"
T = "b"
print(obj.backspaceCompare(S, T))

S = "y#fo##f"
T = "y#f#o##f"
print(obj.backspaceCompare(S, T))
