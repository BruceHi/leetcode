# 692. 前 k 个高频单词
from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        return sorted(counter, key=lambda x: (-counter[x], x))[:k]

    # 未能成功
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    #     counter = Counter(words)
    #     count = list(counter)
    #     queue = count[:k]
    #     heapq.heapify(queue)
    #     for key in count[k:]:
    #         if counter[key] > counter[queue[0]] or (counter[key] > counter[queue[0]] and key < queue[0]):
    #             heapq.heapreplace(queue, key)
    #     return queue[]


s = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(s.topKFrequent(words, k))

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(s.topKFrequent(words, k))

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
print(s.topKFrequent(words, k))

print('i' < 'love')
