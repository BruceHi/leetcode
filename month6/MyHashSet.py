# 设计一个哈希集合
# 使用了 set
# class MyHashSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.res = set()
#
#     def add(self, key: int) -> None:
#         self.res.add(key)
#
#     def remove(self, key: int) -> None:
#         if key in self.res:
#             self.res.remove(key)
#
#     def contains(self, key: int) -> bool:
#         """
#         Returns true if this set contains the specified element
#         """
#         return key in self.res

# 另一种取巧的方法
# class MyHashSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.map = [False] * 1000001
#
#     def add(self, key: int) -> None:
#         self.map[key] = True
#
#     def remove(self, key: int) -> None:
#         self.map[key] = False
#
#     def contains(self, key: int) -> bool:
#         """
#         Returns true if this set contains the specified element
#         """
#         return self.map[key]


# 使用单独链表法，会超时的。
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Bucket:
    def __init__(self):
        self.head = Node(0)

    # 添加到头结点之后
    def insert(self, value):
        if not self.exists(value):
            new = Node(value)
            new.next = self.head.next
            self.head.next = new

    def delete(self, value):
        pre = self.head
        while pre.next:
            cur = pre.next
            if cur.val == value:
                pre.next = cur.next
                return
            pre = pre.next

    def exists(self, value):
        cur = self.head.next
        while cur:
            if cur.val == value:
                return True
            cur = cur.next
        return False


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucket = [Bucket()] * self.keyRange

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        index = self._hash(key)
        self.bucket[index].insert(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        self.bucket[index].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = self._hash(key)
        return self.bucket[index].exists(key)


hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))  # 返回 true
print(hashSet.contains(3))  # 返回 false (未找到)
hashSet.add(2)
print(hashSet.contains(2))  # 返回 true
hashSet.remove(2)
print(hashSet.contains(2))  # 返回 false (已经被删除)
