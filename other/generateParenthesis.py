# 有效的括号
# 下面解答是错误的，正确的还不会。
class Solution:
    def generateParenthesis(self, n: int):
        if n == 1:
            return ['()']
        if n == 2:
            return ['()()', '(())']
        first = []
        for i in self.generateParenthesis(n-1):
            for j in self.generateParenthesis(n-2):
                first.append(i + j)
        return list(set(first)) + ['(' + x + ')' for x in self.generateParenthesis(n-1)]



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
