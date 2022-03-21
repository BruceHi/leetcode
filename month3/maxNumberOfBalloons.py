# 1189. 气球的最大数量
from collections import Counter


class Solution:
    # def maxNumberOfBalloons(self, text: str) -> int:
    #     count = Counter(filter(lambda x: x in 'balloon', text))
    #     if len(count) != 5:
    #         return 0
    #     dic = {}
    #     for k, v in count.items():
    #         if k in 'lo':
    #             dic[k] = v // 2
    #         else:
    #             dic[k] = v
    #     return min(dic.values())

    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(c for c in text if c in 'balon')
        count['l'] //= 2
        count['o'] //= 2
        return 0 if len(count) != 5 else min(count.values())

s = Solution()
text = "nlaebolko"
print(s.maxNumberOfBalloons(text))

text = "loonbalxballpoon"
print(s.maxNumberOfBalloons(text))

text = "leetcode"
print(s.maxNumberOfBalloons(text))

text = "lloo"
print(s.maxNumberOfBalloons(text))

