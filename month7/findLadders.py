# 单词接龙
from typing import List
from collections import deque
from collections import defaultdict


class Solution:
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     word_set = set(wordList)
    #     if endWord not in word_set:
    #         return []
    #
    #     def ischange(A, B):
    #         count = n = len(A)
    #         i = 0
    #         while i < n:
    #             if A[i] == B[i]:
    #                 count -= 1
    #             i += 1
    #         return count == 1
    #
    #     tmp, res = [beginWord], []
    #
    #     def dfs(begin, end, word_set):
    #         if ischange(begin, end):
    #             tmp.append(end)
    #             res.append(tmp)
    #             return
    #         for word in word_set:
    #             if ischange(begin, word):
    #                 tmp.append(word)
    #                 word_set.remove(word)
    #                 dfs(word, end, word_set)
    #                 word_set.add(word)  # 会打乱原有顺序
    #
    #     dfs(beginWord, endWord, word_set)
    #     return res

    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     if endWord not in wordList:
    #         return []
    #
    #     def ischange(A, B):
    #         count = n = len(A)
    #         i = 0
    #         while i < n:
    #             if A[i] == B[i]:
    #                 count -= 1
    #             i += 1
    #         return count == 1
    #
    #     tmp = [beginWord]
    #
    #     def dfs(begin, end, wordList):
    #         if ischange(begin, end):
    #             tmp.append(end)
    #             return
    #         for i, word in enumerate(wordList):
    #             if ischange(begin, word):
    #                 tmp.append(word)
    #                 dfs(word, end, wordList[:i] + wordList[i+1:])
    #                 # word_set.add(word)  # 会打乱原有顺序
    #
    #     dfs(beginWord, endWord, wordList)
    #     return tmp

    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]):
    #     dic = defaultdict(list)
    #     n = len(beginWord)
    #     for w in wordList:
    #         for i in range(n):
    #             dic[w[:i] + '*' + w[i + 1:]].append(w)
    #
    #     queue = deque([(beginWord, [beginWord])])  # 列表里面是一个一个的元组
    #     visted = set()
    #     res = []
    #     while queue:
    #         w, path = queue.popleft()
    #         if w == endWord:
    #             res.append(path)
    #         visted.add(w)

    # bfs，以后要多看看，没怎么看懂
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     wordList = set(wordList)
    #     dic = defaultdict(list)
    #     n = len(beginWord)
    #     for w in wordList:
    #         for i in range(n):
    #             dic[w[:i] + '*' + w[i + 1:]].append(w)
    #     q, s = deque([(beginWord, [beginWord])]), deque()
    #     seen = set()  # 访问过的结点都要记录
    #     res = []
    #     while q:
    #         while q:
    #             w, path = q.popleft()
    #             if w == endWord: res.append(path)
    #             seen.add(w)
    #             for i in range(n):
    #                 for v in dic[w[:i] + '*' + w[i + 1:]]:
    #                     if v not in seen:
    #                         s.append((v, path + [v]))
    #         if res: return res  # 先有结果的自然是最短的
    #         q, s = s, q  # 因为要交换，所以两者的数据类型应该相同。
    #     return []

    # 看得一脸懵逼
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        # 同一组的转换放一块：该无向图相当于邻接表的存储方式
        dic = defaultdict(list)
        n = len(beginWord)
        for w in wordList:
            for i in range(n):
                dic[w[:i] + '*' + w[i + 1:]].append(w)

        queue, tmp = deque([(beginWord, [beginWord])]), deque()
        res = []
        visited = set()
        while queue:
            while queue:
                w, path = queue.popleft()
                if w == endWord:
                    res.append(path)
                visited.add(w)
                for i in range(n):
                    for v in dic[w[:i] + '*' + w[i + 1:]]:
                        if v not in visited:
                            tmp.append((v, path + [v]))
            if res:
                return res
            queue, tmp = tmp, queue
        return []


s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(s.findLadders(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
print(s.findLadders(beginWord, endWord, wordList))
