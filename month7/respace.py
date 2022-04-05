# 恢复空格
from typing import List
from pprint import pprint



class Solution:
    # 动态规划
    # dp[i]: 表示考虑前 i 个字符最少的未识别的字符数量。
    # s[i] 对应的正好是 dp[i+1]
    # sentence[j:i] 对应的正好是 dp[j+1] 到 dp[i] 的值。
    # 官方题解 dp[i]=min(dp[i],dp[j−1]) ，要写成下面的 dp[i] = min(dp[i], dp[j])
    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #     dic = set(dictionary)
    #     n = len(sentence)
    #     dp = [0] * (n+1)
    #     for i in range(1, n+1):
    #         dp[i] = dp[i-1] + 1
    #         for j in range(i):
    #             if sentence[j:i] in dic:
    #                 dp[i] = min(dp[i], dp[j])
    #     return dp[n]

    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #     dic = set(dictionary)
    #     n = len(sentence)
    #     dp = [0] * (n+1)
    #     for i in range(1, n+1):
    #         dp[i] = dp[i-1] + 1
    #         for j in range(i):
    #             if sentence[j:i] in dic:
    #                 dp[i] = min(dp[i], dp[j])
    #     return dp[n]

    # 错误
    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #
    #     # 逆向字典树
    #     root = {}
    #     for word in dictionary:
    #         node = root
    #         for char in reversed(word):
    #             node = node.setdefault(char, {})
    #         node['#'] = '#'
    #     pprint(root)  # 多行打印
    #
    #     n = len(sentence)
    #     dp = [0] * (n+1)
    #     for i in range(1, n+1):
    #         dp[i] = dp[i-1] + 1
    #         node = root
    #         for j in range(i-1, -1, -1):
    #             if sentence[j] not in node and '#' not in node:
    #                 break
    #             if sentence[j] in node and '#' in node:
    #                 dp[i] = min(dp[i], dp[j+1])
    #                 break
    #             node = node[sentence[j]]
    #     return dp[n]

    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #
    #     # 逆向字典树
    #     root = {}
    #     for word in dictionary:
    #         node = root
    #         for char in reversed(word):
    #             node = node.setdefault(char, {})
    #         node['#'] = '#'
    #     # pprint(root)  # 多行打印
    #
    #     n = len(sentence)
    #     dp = [0] * (n+1)
    #     for i in range(1, n+1):
    #         dp[i] = dp[i-1] + 1
    #         node = root
    #         for j in range(i-1, -1, -1):
    #             if sentence[j] not in node:
    #                 break
    #             if sentence[j] in node and '#' in node[sentence[j]]:
    #                 dp[i] = min(dp[i], dp[j])
    #             node = node[sentence[j]]
    #     return dp[n]

    # 最后一个例子错误
    # 找出错误原因：
    # 1. 输出错误的 dp 结果，对比正确答案的 dp,分析从哪里开始错误的
    # 2. 验证错误点
    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #     n = len(sentence)
    #     dp = [float('inf')] * (n+1)
    #     dp[0] = 0
    #     for i in range(1, n+1):
    #         flag = True
    #         for d in dictionary:
    #             if sentence[:i].endswith(d):
    #                 flag = False
    #                 if i == 30:
    #                     print(d)
    #                 dp[i] = min(dp[i], dp[i-len(d)])
    #         if flag:
    #             dp[i] = dp[i-1] + 1
    #     return dp[n]

    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #     n = len(sentence)
    #     dp = [float('inf')] * (n+1)
    #     dp[0] = 0
    #     for i in range(1, n+1):
    #         flag = True
    #         for d in dictionary:
    #             if sentence[:i].endswith(d):
    #                 flag = False
    #                 if i == 30:
    #                     print(d)
    #                 dp[i] = min(dp[i], dp[i-len(d)])
    #         if flag:
    #             dp[i] = dp[i-1] + 1
    #         else:
    #             dp[i] = min(dp[i], dp[i-1]+1)  # 即使当前单词可以匹配，也能选择不匹配的情况来求最优值
    #     return dp[n]

    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #     n = len(sentence)
    #     dp = [float('inf')] * (n+1)  # 注意这里是 无穷大，因为后面是先进行 比较的
    #     dp[0] = 0
    #     for i in range(1, n+1):
    #         for d in dictionary:
    #             if sentence[:i].endswith(d):
    #                 dp[i] = min(dp[i], dp[i-len(d)])
    #             dp[i] = min(dp[i], dp[i-1]+1)  # 即使当前单词可以匹配，也能选择不匹配的情况来求最优值
    #     return dp[n]


    # def respace(self, dictionary: List[str], sentence: str) -> int:
    #     n = len(sentence)
    #     dp = [0] * (n+1)
    #     for i in range(1, n+1):
    #         dp[i] = dp[i-1] + 1  # 这里是进行赋值之后比较，所以不需要 float('inf')
    #         for j in range(i):
    #             if sentence[j:i] in dictionary:
    #                 dp[i] = min(dp[i], dp[j])
    #     return dp[n]

    def respace(self, dictionary: List[str], sentence: str) -> int:
        dic = set(dictionary)
        n = len(sentence)
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            for j in range(i):
                if sentence[j:i] in dic:
                    dp[i] = min(dp[i], dp[j])
        return dp[n]




s = Solution()
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
print(s.respace(dictionary, sentence))

dictionary = ["looked"]
sentence = "looked"
print(s.respace(dictionary, sentence))

# dictionary = [
#     "ioxxoooooxoiooixxoixixxioooxioixixooooiiixoxioioioixooxiiioiioxiiiiiioxoioxixxioxxioxixxxxxooooxioxoiiooiixxixooioxixxixixixooxoixoiiooxiioiiixxxxxixiiioxoxoooooxxoiioixiixxxxioioioxxoooiooiooxoiiixxoxiioiiioioxixxoxioixixxxxixxoxoiixioxioxiooiixoioioxiooooioxiioiooxiioiiixxioooxiiooxioioxxxoiixoxooiooiiixxooooxoioiixoxixxxxxxoxoioxoxioxioxixoooxioxiiioixiixooiixxoxxoiioi",
#     "iiiioxo",
#     "xixooiooxoxxxioxixxiixxoiiixoioioxxxiiiixooioixoxoiioxxoiooooxxixxoxoxoxioixiioixoxixiiiixioxooooooiioxiixiixxiiooiiooxxxxioixiixxoixxioxxxx",
#     "io",
#     "oixioiixiiooxooiooioxxixoioioxxioiiioxixoxoooxxoooixoxxixixiiooioiioxxooiixxoioxxiiioxiioooiooiixooxxoxixixioxxxoiixoxxxioxixxioxoxoxoxoixxxxiooioxiiooxoiooxxooixixoixixixiiixioooiiiiixooxiiiioxoxoixxxxixioxioxxxxoixixxiiixxi",
#     "oooioxioxxiooiiiooixiioiiiioiioxioxixioxxoxiixxiiooxxioixoooxix",
#     "xxoixxoxioiiixioooioooixiixioxxoxoxoxxxxiiiiiixiioiioxoooxxxoioxoiixxooooiiioxiiixiooioixioxiixoxoxiixooxioxoxoiixoooioiiooxiixxoxiixxxoxxxiiooxooixoxoiioxxoiooxixixixxixooiiixxxoooxxooooooxioxoxioixiiiiiiixoiiixooiioxixoioxoxixxxoxxixxoiiioxixxiiixxioxooxoixixioioxiox",
#     "oi", "ox", "xoox", "iixixooooxiixixiioxxxxoxxioiiioixixoxxxiioxooxxioiiioxooixooixiooxxxx",
#     "xxxxooxoixiiioiioxooooxioxxxxoixixooo", "ixxxiioi", "xoixxx", "iooiixiixiixixxxoxxxooxxooxoxxioxxo",
#     "xxioxxoxooooxioxxxxoioxoxxiixixxxixiooxxixiixiooiiooiiioooxxxxxoiooioixxooiioioiixxoioxioixoxxioiixxxoxxooxooooixixxxoxioixoxxoxoxixixiooxiioixiooooiiooooiooixxiixoioxoiioxoixixiixxoioioioiixiiioiooxoxxiiioixixooxioixoiooiiixxxixoixxixiioox",
#     "ooxxioixoixxxooooioiioxixiixoxxx", "xoxixoioixiooiioixixooioox", "oxxoixoxxxoxoxxoxooixooioiioo", "ii", "xi",
#     "oooxiooxooiiixiiiiiixoxoixioxioxixixxxxxooxixoxxixoixxxixxxooooxix", "oiioooixxxooixixxoioioxooixxiixooxxoxx",
#     "oixooxxoxioioxxoooooixxiiiooxioxixooxoxioxixiooixxioxoxioiixxoooxoiooiixxiiiooxooxixiiixoioxooiixooioxoxxiiioioioxoixxiioixxoxxiixiioooioxiiooxxiiioxixiooooxxioioixxxooxxoiixoiioiooixooxxxooooooooioiioixxoioixxxiiooxooxxxxioixoxioioxxioiiioixxxioxioxxxoixxooxooxooioxoxoooooioxiixoioioooooxioioioxiixxxioxoxooiiioxixiixooxioooioxxiixoiixxixxiixioooiooooooxoxoooixxxooxioooxxxxxxiiioixxioooooxooiooiiioooxxiixoiixixiioioxoxiioxiixixoxoooxioiixiioixiioiooiooxxoiioiiiixioioxxoiioxoxixoiiooiooio",
#     "ioxiiooixxxoxioooxoiooixioiioixooxiioxioxiooiioioxxiooxxoixxoixixioiooxioioxooxooiioiioxoixxxooixiioixioixooixxoioxoiixooioixxiioxxoioxoxiioiiioxixiooixioiixoxxooiixoiixxiiioiooiixoiooioxxxxooioxoixiixiixoxoxxoxxxioiixiiioixioxxxxxoxoxiioiooxxxoxixoixxxixixoio",
#     "oixi", "oi", "ooxx", "i", "oxoiixooxx", "xoioooioo", "ox",
#     "ioixoixiixxxioixiooixxxxoxxxoiioxxiioxxxxixioixooxxiioxooixoooooxxxixixxxioxxoxiioiioioxxiooiiiioixiooxiooiooxooxxoooixxxxiioiixoxoooixxiixiioiiixoxxxxioiiiixoxioxxioioxxxi",
#     "oooxo",
#     "oiooiioxoxxoiooioooiioxxxooioiixxixixiixxoixxxooxixxoixoioxxoxoiixoxxoxixoxioxiooxiioiixooioioiooiixxxioxxiooxxoiioxioooxoiooxoiixooxiooixxxxooiioixoxiioooiiixxxoiixooixoiiioiixiiiiooxoooxoixxixxoiiooxxixiixoiooioooooiiiioixoixioxxixioxxiiixixxxxioxoxoiiioxixiooioxxixoxxxoxxxxxoixxoxioxoxxooxixoxxixoxoooooxooxioixxxooooxiixxxoixioxiixioxooixxxoxxoiixiioxiiixioxooooiooxoxixxooiooxoxoxxoooxxixoixooooxioxoxxxoxxixoxiixxxxox",
#     "i", "oooi",
#     "xxxxixixxxxoixioioxoiioiioixxixxioiixoxoooiiooooiioxiooxixooooooxxxioxixoiixiiooixoxxxoxiooxiooxoixxiioiiooioixxxxixxxoiiiioooiiioxooxxioiiiooixoioixoxiixixxiioxixioooxiiioooxoioxxxiixiixiiiixxxiioxoooxiooxxxoioxiioooxixoiiooixioiixiioxxoixx",
#     "xooiiixxioo", "oxiooo",
#     "iooxooioiiooioixoxoxxooxoxioxxxoiooxoioxioxooioooixxxixixoiixxixixxoixxoxioxooiixooxxixxoiooxxoxxixxiioxioxoxiiixixiixoxxxxioiiioooxooiiixxoixiiiixoxiixoxoiiiixooxixoxoiixixixooxioiooiioxoxxoxoxoiioxoxxioxooooxoxixxixoxiiixoixxxo",
#     "ioxoiiooixxoooioioxoioxooooxiixoiooixixoixxxiixooxixxixxixoxxxxiiixixxxioioxoixxioixixioxixoxxooxoxoxooxxoxixxoxxoioiixooixxoixixoxxooixxoiixxixxooxooixxiixiiiiioiooioixoooxoxxoxixoiixoxiiiiioooiooxxxixoooixxoixooxiiooxxxxioixxxoooiixoixxxixiiiiiio",
#     "i", "ix",
#     "oxxxiixooioooixxxiiooooixoxoixooiiioiioxxxxxixxxoxxxixoiixxxxooixxioxooixiioiixioioioiooxxxxioxxxiooxiixxoox",
#     "ooxxoxiioxxxioxoxxxixxixoxxioiiiiox",
#     "ooixoxxixxxoxoixxooiixoooxxxixiiiooioooiooixiixixxioiooiooiixoiiixioiiooiiiooioioioxoioiioooiioixooxooiixiixxxixoioxoxoiixoiioooiiioiixxoxixoioioxiixoiooixxxioiixoiiiiixioixooxiixioiioooxoooxxoixixoiiioiixoiixixxxxxoxoxoxxooxoxxoiiiixxiixoiixooiiioooioxioxxxoiixxixoiooxxixixoooxoxxxixooioxixoixxxoxxxoxixooiiixiiiioooxioxxxoioxiixxxiioooxxxiiixxoxxoiixoiixxooxoioxi",
#     "oxioiiiooiioxoiooiiioxixxxxoiioxooxxxxxoxooxioiixixoioioxx", "xxiiooxiiioxxxoxxxoiixi", "oox", "xoiiiix",
#     "oixxiooxoixooiixxiixxxoiixoxoxoooixoxxxxixoxixxixxioiioixioxxxixoioixioooxoxoiooiooioiiiiixiooixxxoxiioxxoioxio",
#     "ixxo", "i",
#     "xxiixoxxiixixxoixiooooxoooooxxooxoxioooxoxxixxixioixixooixixxxioxxxxxoxooioioxxooixixxoxxxiioooioxixiixiiooioxoxixoiioooioxoiioixxioxixixoxoioixxoiiixiioixoiixooioixxiiiiixoxixxioixoxxiiiooiiixxiioioooxxoioooxixoixxxiiooio",
#     "xixooiixi",
#     "ioixxxoxiixooxiioxxiixoxxoxoxxxixiiooixixoixixxiixoiixoxoxxixxioooxoiooioxixxoiooxiiixiiioiixxoixiiixxiiixooxoixoxxiooooixoxxxoxiixxxixioooixioiixxoxixiooxoiioiixxixoxiooxxiiooxxxoxoxoioxxxooxoxoxoiooixiiiioiioixxixixixxooxoixxiiooooiiixii",
#     "oiixxxoxxixoxoooioxxoioi", "oiio", "xixxoixoxiixoxiioixoixxiooioxiixixixx", "oxoxi", "ioxxxx",
#     "iixioooooxxxooiixoxxixoxxxiioioixiiioxoixoxoxxioioxxxoixxixxxioxoiiiixxiixixxoxoxoiioxxixixxioiooooixxioioxxxxxoxiiioxiiioxxiioixioiiooxoxioxxxiixooxoxooioxxxoiooioiiiiiooxoooxoiioiixoxoxxiioiioooxiiiiixxxiiiooixxooioxxxx",
#     "oooxoooxiixioxx",
#     "ioxioooixiioooiiixoxooiooxioxiioooxxoxixioioooooxoiooxxioioxoiixxoioxxixiioixixxxoixixoxixixxixxixooioiioxxoxiixixiooxiiixxioi",
#     "ixoixoiooooxxooxixoixooiiiooxoxoxxixxxxxoxiixooxooiixxxixxoxixoxxoioiiioxxxxiooioioooiioxxxxoxoiooixoioixoiixxxiiixxxxoiiiixiioooxxiixxooixxxxoixoixxoxixoxoiioxiixxxi",
#     "xo",
#     "iooioxxoxxxioxixoooiiioxxiioxxooxoiioiooiioxoxioxoxoixxxoioiiixxxixiiiixiooxoxixxxioxixooxiioxioxxoiiixioioxixi",
#     "xooxoxooiooio",
#     "ixxoxoxoxoooooxixiooioixoixoxiiooxxoiixxioioxxiioxoooiixoxxxooxiooxoxxxxoxiixoxixixoxoxoxixiixixxiixioioxioooxixoioiixioxooxoxxoxoxiioooixoxxooiiixixooxoioxxxoxoxoixiooxixxxoixoxxxoixxioxoioioxxxxoiixixxoixoxxiixxxxiioixoxxxiiiioooxoxixoixooxiixiioxxxxoiiooioixxii",
#     "oxoxiiooioixooxxxoixiixoooxxoxxxxoioxoxxxioxxoiooixioxxixoxxxixiooioxoooiiixxooooioxxxoiixioxixxxooioxiioiixxxoxoxioiioooixxiiiooxooixoxoixiiiixiooiiixoixxoixxooiiooooiiixixoixoixioxioioxioxixoxooiooiixiiiiiiixixxoxxoooxoioixxixxioioxxxixiixxxooxiioxoixxxiiixooiixoiiixoxxxxixxiooiiiooxixxoiooxiooxxiiooooiixxxxiioxix",
#     "iiooiooxooxioxxoioioxixxioxxiooxiioiixixioxoixxoxoxxxiiooiiiixoooxxxxiixoioioixxoioiioiioioxoioiooxooioxxxoooioooxoxooxixoixiooxooxxxxxioxxxxoooxoioxxxiioxiiooxxxxiixixixoxioooxoxxooixoxioiioxoioxoixiioxooxxxoiixoixixixxoxiiioixoixxooxiooxxoiiiooooxiixixiixxxiiooiooxoixixoixooxioixioxixoxixoioiioiiixxxooxxxxoiixoiixooiioixioxxoxxxixixxioxiiiixoxoxiixoooioiixioxoioixioxoixxooixixoioiiioiixxiixoooooooxxoxxoxxixiiixxxixoxoixxiioxoiooiixxxooxxoxoixxxoxioiixioo",
#     "ixoxixxo",
#     "oixxxxixooxoixoixioxooxoiixoiooioixioxoiooooxixooxxiiiiiooixxxoixoixxixxiooioxiioxxoixxixxoioiiooioxooooixxoiiixiooiixoxoxioiiooxxixoxiioixoixxioooiixiiixxoioooxioixxioixxoxxiioioiioxxioxioiooiiiiioxoiiioixxxiiooiiooixxooixoxiiooiooiixxiixioiiiixiooxoioiixxxioo",
#     "iio",
#     "oioxoxxxxiiiiiixxoixxxiixoxoiooooiooxoxoioixxooxiiixoxooxoixoixixixioiiioxixiixxixxoioixoxixioixixoxioxioioixixoiiiiiixixoxoixixxioooiixooxxoixoixxioioxxoxxioixiooioxioioioioiiooxiixxxoxioxxoioxoooixiioxixio",
#     "ioiiiiixoixoooixooooixoooxoiooxxxxixxooxxixixiiioxxioioiooiixoiooooooixxxxoxxooxoioixixoxioxixooixooioxioxiooooxxxixioxiooxioixooxioiiixxooixxxxxxooxoooiiiiooiiiixxixixoixoxioxoixioxxiixixo",
#     "xiox", "ioixiixxooxiiixooxiioxxoiixoiooxoooioxooixoxo", "iiooxxxoxxixxxooixioioooxxixoxioxiiioxooiiiioiooiiooxoi",
#     "ioxxxooxxxxiiiiixixixioiixoxooxixxioixiixxiioxxixxoioiixioiioooiiixoioxiooiiiioioxixixoxxooioixioxioioiioiooixoioooiioxxxixoxiixiooxoxixiooiiioxoixxixiiooioxooixooiiioiixiiioooiioxioiiooxiioioooxioxxioixioxoooxooixioiiixooixioxoxixioxoioiiioixioxoioooxioiioixiixioiiixxxxioiiixxiiioixxxiooxooxioxxoxoooxooixxixooixixiiiioiiooixxoxoioxiooioixoxooxooxooixooiixxixixxoioixoioxiiixooxxoxoioixioixiixxiixoixoooxxixxxxoixioo",
#     "xiioxoxoiooioooxxioooixiixiooxoixxiiooixxixoiioixoxoxooxxoxiiixixiooiixoooiixooxioxixoxxoiiixooxixxxixiiioxxxiooxxoxioooxxixooiooiioxixoxxxoixxixxixixioxioxixxxoxooxxixoixooooiooxxoxixxixxxixooxoooxxoixxo",
#     "ox",
#     "oixxiixixxixioooooioixoxxoxoiiixxooxxoioxoooooxoxxiioioxoiiixiixiiioiiiiiioxiiixiiooiioooxioiiiooixxoixoxxoioixxiiixixxioiiioooioio",
#     "xxoixiioo",
#     "xiooxxixooxxxioxixxoxoooioiixooiixxxiixixxxiixooiixixioixiiiioiixooxiiiiiixxixooooxoooixiiixxixoooxoxixioxixixoiiiiixioiiiixxoiioixxxoixiioxixoxxxixxxiiiixxixxxxoxiooixoxxxoxooxoxooixxooioiiooixioxooxxxoooixoxiixixooxixoioxxxooxoixioiioxxiooxxxxixioooxiooixxxixooiioxoooxiioiixooioixoxiooxixoixxxxxxooixoxox",
#     "oxioiioixooioxxoixxi",
#     "xixxxiiiiixiixxiioiixooooiixxiixooiioxiiixxoooxxxoxioixxiixxxxoooixixixiioiiooioxoxooioxxoiooxooiixx",
#     "ixiioixixiixooxoixixixiixoiooxiiooixxoooixxoxioioixiiiiixoixixxxxxxxioxooxxixoioxixxiiixoxiixooxoixoiiixoixooooixxoioixxixxixoooxoxoxxoooooxoooxoiiiooxixooiiiiioxxoioiixioxoxxioxoxoxoixxixixoxxxoxiixiooxoixixoiixxioxxixxxxoixixixioixxixiiioxooxxxixxoxiiixxoiixoxoioioxxiioixooiixoxioxoxxoiioxooioxoioxixixoxxixoiioiiioxooixiioixxoiioxxioxooiixixxooooxxixxoioioiiiiixxoioioixxioxxxxxoxiooooioxoxiioioxiixiioxxiiiooiiiooxixoxixooooioixiiiixixooxoxxixixixoxixiiixioxoiiixooixixox",
#     "xxxoxoiixixxoixioiiiooxxooooxxixxxxoiixiixxiixooiioiiixoooxoiooiiixioxoxixxxioxiiioixxiooxiiixioixooooixixoioxxxxxoioxiioxxixooxxxxoxxxiooxooooxxixxxioxixxioxoxxiooxioxiooixxoiooxiixxxixixoioixooxxiiixxoioxoxioxxxiooioxixoxiiooxxxxoioiiiiioxoxixioiiiiioxoiixiooooioixiiioxxoioiiioxiiioxioooxioxooixiiiiiooixoxiiixxoxoixooixxioxxioooioiixixiooxiixixxoooooixxoioixixxxiioixxoxixixioooioxixioooioooxiixiooooxooxxoxxoxixoixiioiioioxxxxixooxxo",
#     "xiiixxixiioooxxixioixoxooxoiooioioioiixooxoxoiioiioixxixxxoooxioioxoiooioiioxixxoxxxxooixiiixxxoioxoxoooxioiioxxixxoooxoixixoxxxoixixxxiiiiioxoixoxiixooxoiiooxxxoxxiooixxxoxioiooiioxxooioooxxoxooioxoxxoxioxoxoiixxxooiixiioiixoixoxiixoxixooooooiiioiixxoioxoxiiioixxooxooioxiioooxiiiiiioiiixoioxixxxioixxooxxoiooxxxxoioiiooooxiixxxioxxxxioiixiixxxxiioiiixxxiioxioooooooioxoiioxooooxoiiiioooxoxioiixooioooooioxoixxoooooiixxixooixxxioiixixixxxoxoxxixiixxxxoixoiooxxiioioxixixixoxioiooixxioiooixxiixoooioii",
#     "ixoooi", "ioxoxoioooiixxoioxoixiiiiooxxiioxxxoixxioxi", "xiioooooioox", "oo", "o", "xooioixx",
#     "oixxioooioixooxoixxixixooiiooxooioxixxioxiiixoixixxxoioxxxooxxxooxoiixxxooxioiooxxioxoioioooxoiooxxioixxxxooixiixixoiiioixoooixxxxoxxxoioiooixxoxxiixooixoiioioixxxoixxoixxoxxxoooioxoxixooxoiixooixxxixoii",
#     "xioooxxxxoixiooxxixix", "o", "oxiooxxiixixiixixxiiooixixoiiioxooxioxxiiiioiooxixxoxoiiiooixxoixoiioxiiooiooi",
#     "xxxixoxxxxiixoiioooooxxiooixxxiixxiooxxixooxiixooxixxiixixoixixxoio",
#     "xiixxiixoxoooxoixiioiioioioioxiooxxoixixoiooxixxixiioooooixoxoo",
#     "oixoixxoxioxoxxxoxoioixooiiooxxooiooiiioiioixxoiiixixxioxoxxixiiooxoiioxioiioxoxooixxxxxiixxxxxiioxoxo",
#     "iooioxoxoixxxxoioixixoxoixixioxioxoxxxxixoioxxxoooiioiiioixxoxoixoxxiio", "xoxi", "ixooxooooio",
#     "xixoxoxioxoixioixxoxixoxoiioxoxiiiiooxxxooxoxioxxioiiixxoxoxiixxoixioxxoixioixixoxxioxoixoxoooxoxxxioxoooiooioiixixxxixxxxiioiiiooxiooxxixoxooioixxoixxoixoxiooiixooiooixoiixoiioixxioxoioooxoxioiixoxiiioxoiiiixxiiiooioiioixixoooxixxiooioxoxoxxxooooxxiiioioiiixoxioxoioioiiioiiiiooixoixixixoxioxioxiioxioooiiioxxiooxo",
#     "oiixoioixooxxixoxoxooixoxiixoixx", "iooo",
#     "iixxioiooxoioiixxoxxxxoioiioiioooioioiioiooooooixoxooxxiooxxiiooxixxxoiiixiiiixoxoxixxxoiixooioxxxxxooixooiixioixiioxxooxooioooiixooxoiooxoiixxioooooiioixxooiixioioxiooxoiioiooooooooooxxioxoioxxiixoixiooooiooiiiixiiioio",
#     "xooxxioxixoiioixxixxxxxooxixxoiooooxiooxiiixooooiioooxixoxxooxoiooixxxxoxxoiooxxoxoiixooooxoiiooxxoxiooxoixoxixiixoxooxioiiixxixoxxxxooioixoixooioiixoxixooioiiiiooxoooxioxxiooioiixiioixiiioxiiooooxixooixoxioiiiioxxxoxxixxoxiixiooooixxiooioxoxoxiiioiooxxooioiixoxoxooiiooiooxxoxxxoxioxiiixxooixxixxioxoixiooiixxooiixoioxxoxioxioiixoxxxixoixxoixioxoxoxxooxxiiiioioxixiiiixiixixioixiiiioxoiiiiooxxoxxoi",
#     "xxoi", "iiixxixxioxixoooxiioooioioioxoioooxiiooooxixxxixixiooioixixoxxoxooixioixxxoxiixxixoxiii", "iioi",
#     "oixioxxxoooixoooxio",
#     "iooooioxxoxixixixoiioixoiiixxxixoiiiiioxixxioxxoxixoioioiooxxxoixioiixiiiiooixixoixxooxxxoixooiixxxxoxixioxioixooiioxixxioiiixixo",
#     "ooxixioxoxxoxoxiiiioxoixoixxiixioxxixxxxxioixoxxxoioiiio",
#     "oooxxoioxiooxooiiiooxxxooxoixoxioioioixxiooixooxioixiiiooxxoooxxxxixiooooixxxixoooioixoixooiiix",
#     "iiixoxixxoioxxoixxxoixxoxiioixoxioixiixiioixxxoxioooxioioxixioixxoxiooxxixoxixiixiioiixxixoxiioiiixooiiioioxooxoxioooixoxxxxxxxoxooixxixixxioxooxiixxoixioiiooiixixxioioixxoxooxixooxxoixoxiixixioiiioxoxxoxoioixioiiixiiiooxoixxxioxixooxiixioxooioooixixoiiioooiiioioxxoiixoxxoxoxoiooooiooxxooiiiooxoiooiooxxixioxxxxxiiooiiooixxixiooxixiixoxiixxxxxoiixiioxxoxxoiiioooiiioxioxiioiixioioioxoxixxxxxoxxooioooxoiixooxxixoiiiixixoioxxiiixxxx",
#     "xxoxoooiioxxoiixoxoxiixxxixoixooxxiiixxoooxx", "xiiiixxxiooixxxiixxiooxxioxixixxixoixxooiiooooooiixoxoixxi",
#     "oxxioiiixoxxooixxxixioioiiixiiiiixoxxiixxoioxxiixooixoiioxoioooxxxixxxxiooiioxoxxiixiioxiixooiixiioxooooioioxooxoooioiioxxoioxxoiiioxxoooiixoxixixxoixxixoxxixiioioixxiooxioioxiioiioixxxxxixxxooixxxixoooxxioxiixxoooioioiiixooioooooiioioxoxxiioxooxxxioooxoiiiixixooixoooxioxoxoixooxoiiiiixxxxoxoixoiioixixxxx",
#     "oioiooiixioxxoixxoxxxoxxiixoxoioxooiooxxooxxo", "ixix",
#     "iiixiioxxoioiiixxxxoooxoixxoxxxoioxooxxooioxoiixixoooiooxoxxxoiioioixxixxiixoiioxoiixxioxioxooixooioiiiooooiiiioxxxxiioioxixioiixoixioxoioxioxxxoiiioxxxiioxooxoioxxoixoooxioioioioxooioxoxxioxoxoxxixxiooiioxiioooooioixooxiiioxoioiixxxixxiixxoiixixixxixxooooxoxioiioxixiiooxixxxxioooioxooooxxxiixoxoiooixxxooooooixxxoxioooxxxxxxiooooooxoxoxioxxixooxxoioixxiooixoxoxixxxxiioixioixxxoxxxixoxxoxiixxoiiixixixiiioxioixoixixoxooiiiixxxiooioooiooiioxoxioixoiioiixxixoixxxxoxxxiixoixoiooxxoxioiiixxxixxooioxoooxxxooo",
#     "i",
#     "xxioioxoxoixoxixxoiooiixioiooxooxoxooioiixooixoioooxxioioxixxoixixiioxiixoxioxxixxioxxxixooooioxoxoooixxxxoooxoxxioxiixoiioxxxioxooixixoooxooixxxxxiiioixooixxxxioxoxoxxxxxiiioiioxoixoxoxioxioiixiixoxxxoiioixoixixixxixioiiooixoiiioxooixixooioxxiixxoixixooioxixiiiooxxixxiiiixoxxxooioiixxiixxioxixoioiiiiixoxoxxxoxxioxxixoxxxooixxioxoxoooooxiiioxxxooxxooixiixoooiiiioixxoooxioiiioooxioxox"]
#
#
# sentence = "oxxoixoxxxoxoxxoxooixooioiiooxoxixxxiioixoixxxiooioxxoxxxioxixoooiiioxxiioxxooxoiioiooiioxoxioxoxoixxxoioiiixxxixiiiixiooxoxixxxioxixooxiioxioxxoiiixioioxixioooxoxooxxioxixoiioixxixxxxxooxixxoiooooxiooxiiixooooiioooxixoxxooxoiooixxxxoxxoiooxxoxoiixooooxoiiooxxoxiooxoixoxixiixoxooxioiiixxixoxxxxooioixoixooioiixoxixooioiiiiooxoooxioxxiooioiixiioixiiioxiiooooxixooixoxioiiiioxxxoxxixxoxiixiooooixxiooioxoxoxiiioiooxxooioiixoxoxooiiooiooxxoxxxoxioxiiixxooixxixxioxoixiooiixxooiixoioxxoxioxioiixoxxxixoixxoixioxoxoxxooxxiiiioioxixiiiixiixixioixiiiioxoiiiiooxxoxxoi"
# print(sentence[:30])
# print('----')
# print(s.respace(dictionary, sentence[:30]))
