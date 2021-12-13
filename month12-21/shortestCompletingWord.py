# 748. 最短补全此
from typing import List
from collections import Counter


class Solution:
    # def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
    #     count = Counter(map(lambda s: s.lower(), filter(lambda x: x.isalpha(), licensePlate)))
    #     res = 'a'* 16
    #     for word in words:
    #         if count - Counter(word) == Counter():
    #             if len(word) < len(res):
    #                 res = word
    #     return res

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        return min((word for word in words if not cnt-Counter(word)), key=len)


s = Solution()
licensePlate = "1s3 PSt"

words = ["step", "steps", "stripe", "stepple"]
print(s.shortestCompletingWord(licensePlate, words))

licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
print(s.shortestCompletingWord(licensePlate, words))

licensePlate = "Ah71752"
words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
print(s.shortestCompletingWord(licensePlate, words))

licensePlate = "OgEu755"
words = ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]
print(s.shortestCompletingWord(licensePlate, words))

licensePlate = "iMSlpe4"
words = ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]
print(s.shortestCompletingWord(licensePlate, words))
