# 等式方程的可满足性
from typing import List

class UnionFind:
    def __init__(self):
        self.parent = list(range(26))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # 未使用按 rank 合并
    def uoion(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        index = ord('a')
        for s in equations:
            if s[1] == '=':
                index1 = ord(s[0]) - index
                index2 = ord(s[3]) - index
                uf.uoion(index1, index2)

        for s in equations:
            if s[1] == '!':
                index1 = ord(s[0]) - index
                index2 = ord(s[3]) - index
                if uf.find(index1) == uf.find(index2):
                    return False

        return True


s = Solution()
a = ["a==b","b!=a"]
print(s.equationsPossible(a))

a = ["b==a","a==b"]
print(s.equationsPossible(a))

a = ["a==b","b==c","a==c"]
print(s.equationsPossible(a))

a = ["a==b","b!=c","c==a"]
print(s.equationsPossible(a))

a = ["c==c","b==d","x!=z"]
print(s.equationsPossible(a))
