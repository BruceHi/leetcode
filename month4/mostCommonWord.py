# 819. 最常见的单词
from typing import List
import re
from collections import Counter


class Solution:
    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #     p = re.split(r'[ !\?\',;.]', paragraph.lower())
    #     count = Counter(p)
    #     for k in sorted(count, key=count.get, reverse=True):
    #         if k and k not in banned:
    #             return k

    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #     paras = re.split(r'\W+', paragraph.lower())  # 去掉连在一起的非字母数字下划线
    #     count = Counter(p for p in paras if p and p not in banned)
    #     return count.most_common()[0][0]

    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #     paras = re.split(r'\W+', paragraph.lower())
    #     count = Counter(x for x in paras if x and x not in banned)
    #     return count.most_common()[0][0]

    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #     paras = re.split(r'\W+', paragraph.lower())
    #     count = Counter(x for x in paras if x and x not in banned)
    #     return count.most_common()[0][0]

    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #     paras = re.split(r'\W+', paragraph.lower())
    #     count = Counter(p for p in paras if p and p not in banned)
    #     return count.most_common(1)[0][0]

    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #     count = Counter(filter(lambda x: x and x not in banned, re.split(r'\W', paragraph.lower())))
    #     return count.most_common(1)[0][0]

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paras = re.split(r'\W', paragraph.lower())
        count = Counter(p for p in paras if p and p not in banned)
        return count.most_common(1)[0][0]

s = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(s.mostCommonWord(paragraph, banned))
