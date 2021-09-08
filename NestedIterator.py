# 341. 扁平化嵌套列表迭代器
from collections import deque


class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
       return True

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
       return 1

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :return  -> [NestedInteger]
       """
       return []

class NestedIterator:
    def __init__(self, nestedList: NestedInteger):
        self.queue = deque()
        self.dfs(nestedList)

    def dfs(self, nests):
        for nest in nests:
            if nest.isInteger():
                self.queue.append(nest.getInteger())
            else:
                self.dfs(nest.getList())

    def next(self) -> int:
        return self.queue.popleft()

    # 非空返回 true
    def hasNext(self) -> bool:
        return len(self.queue)


def test(n: NestedIterator):
    res = []
    while n.hasNext():
        res.append(n.next())
    return res

s = NestedIterator([[1,1],2,[1,1]])
print(test(s))

s = NestedIterator([1,[4,[6]]])
print(test(s))
