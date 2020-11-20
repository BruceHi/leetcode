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

    def respace(self, dictionary: List[str], sentence: str) -> int:

        # 逆向字典树
        root = {}
        for word in dictionary:
            node = root
            for char in reversed(word):
                node = node.setdefault(char, {})
            node['#'] = '#'
        # pprint(root)  # 多行打印

        n = len(sentence)
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            node = root
            for j in range(i-1, -1, -1):
                if sentence[j] not in node:
                    break
                if sentence[j] in node and '#' in node[sentence[j]]:
                    dp[i] = min(dp[i], dp[j])
                node = node[sentence[j]]
        return dp[n]


s = Solution()
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
print(s.respace(dictionary, sentence))

dictionary = ["looked"]
sentence = "looked"
print(s.respace(dictionary, sentence))