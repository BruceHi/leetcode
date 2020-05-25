# LRU 缓存
# 其中只有 key 和 value 同时相等，才能看作同一个结点
# key 存在则更改 value


# # 双链表方法
# class ListNode:
#     def __init__(self, x, y):
#         self.key, self.val = x, y
#         self.prev, self.next = None, None
#
#
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.size = 0
#         self.head, self.tail = ListNode(None, None), ListNode(None, None)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     def get(self, key: int) -> int:
#         curr = self.head
#         for _ in range(self.size):
#             curr = curr.next
#             if curr.key == key:
#                 # 删除结点
#                 pred, succ = curr.prev, curr.next
#                 pred.next, succ.prev = succ, pred
#                 pred, succ = self.head, self.head.next
#                 # 头部添加结点
#                 curr.next, curr.prev = succ, pred
#                 pred.next, succ.prev = curr, curr
#                 return curr.val
#
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         # 没找到 key
#         if self.get(key) == -1:
#             self.size += 1
#             new_node = ListNode(key, value)
#             pred, succ = self.head, self.head.next
#             new_node.next, new_node.prev = succ, pred
#             pred.next, succ.prev = new_node, new_node
#
#             if self.size > self.capacity:
#                 self.size -= 1
#                 pred, succ = self.tail.prev.prev, self.tail
#                 pred.next, succ.prev = succ, pred
#
#         # 找到了 key, 但值不同。已经访问过了，位于最前面。注意使用 elif
#         elif self.get(key) != value:
#             self.head.next.val = value


# 使用有序字典：OrderedDict
from collections import OrderedDict


# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.dic = OrderedDict()
#         self.capacity = capacity
#         self.size = 0
#
#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         res = self.dic.pop(key)
#         self.dic[key] = res
#         return res
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.pop(key)
#         else:
#             self.size += 1
#             if self.size > self.capacity:
#                 self.size -= 1
#                 self.dic.popitem(last=False)
#         self.dic[key] = value

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# cache = LRUCache(2)
#
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))  # 返回  1
# cache.put(3, 3)  # 该操作会使得密钥 2 作废
# print(cache.get(2))  # 返回 -1 (未找到)
# cache.put(4, 4)  # 该操作会使得密钥 1 作废
# print(cache.get(1))  # 返回 -1 (未找到)
# print(cache.get(3))  # 返回  3
# print(cache.get(4))  # 返回  4

cache = LRUCache(2)
print(cache.get(2))
cache.put(2, 6)
print(cache.get(1))
cache.put(1, 5)
cache.put(1, 2)
print(cache.get(1))
print(cache.get(2))

