# 884. 两句话中的不常见单词
from typing import List
from collections import Counter


class Solution:
    # def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    #     count1, count2 = Counter(s1.split()), Counter(s2.split())
    #     res = []
    #     for k, v in count1.items():
    #         if v == 1 and k not in count2:
    #             res.append(k)
    #     for k, v in count2.items():
    #         if v == 1 and k not in count1:
    #             res.append(k)
    #     return res

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter(s1.split()) + Counter(s2.split())
        return [k for k, v in count.items() if v == 1]


s = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(s.uncommonFromSentences(s1, s2))

s1 = "apple apple"
s2 = "banana"
print(s.uncommonFromSentences(s1, s2))

s1 = "s z z z s"
s2 = "s z ejt"
print(s.uncommonFromSentences(s1, s2))
