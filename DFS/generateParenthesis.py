# 括号生成


class Solution:

    # # 原始解法，不太好
    # def generateParenthesis(self, n: int):
    #     res = set()
    #
    #     def DFS(s, c, left, right):  # s: 当前拼接到的字符串，c:传入的括号
    #         if len(s) == 2 * n:
    #             res.add(s)
    #             return
    #
    #         s += c
    #         if c == '(':
    #             left += 1
    #         else:
    #             right += 1
    #
    #         if right <= left <= n:
    #             DFS(s, '(', left, right)
    #             DFS(s, ')', left, right)
    #
    #     DFS('', '(', 0, 0)
    #     return list(res)

    # 改进
    def generateParenthesis(self, n: int):
        res = []

        def DFS(s, left, right):
            if len(s) == 2 * n:
                res.append(s)
                return

            if left < n:
                DFS(s+'(', left+1, right)
            if right < left:
                DFS(s+')', left, right+1)

        DFS('', 0, 0)
        return res


s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
a = ["()((()))","(()())()","((()))()","()(())()","(())()()","(((())))","()()()()","(()()())","()(()())","(()(()))","((()()))","((())())","()()(())"]
b = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
for i in b:
    if i not in a:
        print(i)
        break
