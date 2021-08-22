# 电话号码的字母组合
# 当题目中出现 “所有组合” 等类似字眼时，我们第一感觉就要想到用回溯。
from string import ascii_lowercase as letter
from typing import List
from itertools import product


class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:
    #     if not digits:
    #         return []
    #     dic = {str(i+2): letter[3*i:3*(i+1)] for i in range(5)}
    #     dic['7'] = 'pqrs'
    #     dic['8'] = 'tuv'
    #     dic['9'] = 'wxyz'
    #
    #     res = []
    #
    #     def dfs(s, cur):
    #         if not s:
    #             res.append(cur)
    #             return
    #         for c in dic[s[0]]:
    #             dfs(s[1:], cur+c)
    #
    #     dfs(digits, '')
    #     return res

    # # 利用 python 重复地使用 res 形成递归
    # def letterCombinations(self, digits: str) -> List[str]:
    #     if not digits:
    #         return []
    #     dic = {'2': 'abc',
    #            '3': 'def',
    #            '4': 'ghi',
    #            '5': 'jkl',
    #            '6': 'mno',
    #            '7': 'pqrs',
    #            '8': 'tuv',
    #            '9': 'wxyz',
    #            }
    #
    #     res = ['']
    #     for k in digits:  # 遍历数字位数
    #         res = [i+j for i in res for j in dic[k]]
    #     return res

    # def letterCombinations(self, digits: str) -> List[str]:
    #     if not digits:
    #         return []
    #     dic = {'2': 'abc',
    #            '3': 'def',
    #            '4': 'ghi',
    #            '5': 'jkl',
    #            '6': 'mno',
    #            '7': 'pqrs',
    #            '8': 'tuv',
    #            '9': 'wxyz',
    #            }
    #     # 注意区别，前者 iterable 数量为 1，后者有两个
    #     print(list(product(['abc', 'bd'])))
    #     print(list(product('abc', 'bd')))
    #     print(list(product('abc', 'bd', 'efg')))
    #     #
    #     #
    #     print("ha", list(product(dic[x] for x in digits)))
    #     # # print((dic[x] for x in digits))
    #     # # for a in (dic[x] for x in digits):
    #     # #     print(a)
    #     print('ok', *(dic[x] for x in digits))  # 对元素进行解包，比如对 （‘abc’，）解包就得到了 abc。
    #     print(list(product(*(dic[x] for x in digits))))
    #     return [''.join(item) for item in product(*(dic[x] for x in digits))]

    # def letterCombinations(self, digits: str) -> List[str]:
    #     if not digits:
    #         return []
    #     dic = {'2': 'abc',
    #            '3': 'def',
    #            '4': 'ghi',
    #            '5': 'jkl',
    #            '6': 'mno',
    #            '7': 'pqrs',
    #            '8': 'tuv',
    #            '9': 'wxyz'}
    #     return [''.join(tmp) for tmp in product(*(dic[x] for x in digits))]

    # def letterCombinations(self, digits: str) -> List[str]:
    #     if not digits:
    #         return []
    #     dic = {'2': 'abc',
    #            '3': 'def',
    #            '4': 'ghi',
    #            '5': 'jkl',
    #            '6': 'mno',
    #            '7': 'pqrs',
    #            '8': 'tuv',
    #            '9': 'wxyz'}
    #     res = ['']
    #     for digit in digits:
    #         res = [tmp + x for tmp in res for x in dic[digit]]
    #     return res

    # def letterCombinations(self, digits: str) -> List[str]:
    #     dic = {
    #         '2': 'abc',
    #         '3': 'def',
    #         '4': 'ghi',
    #         '5': 'jkl',
    #         '6': 'mno',
    #         '7': 'pqrs',
    #         '8': 'tuv',
    #         '9': 'wxyz'
    #     }
    #     if not digits:
    #         return []
    #     return [''.join(tmp) for tmp in product(*(dic[x] for x in digits))]

    # 使用递归的形式
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        res = []

        def dfs(s, cur):
            if not s:
                res.append(cur)
                return
            for c in dic[s[0]]:
                dfs(s[1:], cur+c)
        dfs(digits, '')
        return res


s = Solution()
print(s.letterCombinations('23'))

print(s.letterCombinations(''))

res = {i+2: letter[3*i:3*(i+1)] for i in range(5)}
print(res)

a, = ('abc',)
print(a)
print(type(a))

a = 'abc'
print(a)
print(type(a))

# 在控制台直接显示单个字符串时，不带引号。
# 组成集合元素时就带引号了。

a = [str(1)]
print(a)
